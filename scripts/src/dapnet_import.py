#############################
# Import the required libraries
import os
import sys
from datetime import datetime, date, time, timedelta
import json
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from io import StringIO

#############################
# Define the global variables
linefeed = "\r\n"
dapnet_url = 'http://www.hampager.de:8080/callsigns' # done

#############################
##### Define Functions

def xstr(s):
    return '' if s is None else str(s)

def print_event_time(event):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(event + " " + current_time)

def data_import(db_engine,pwd):
    event = 'Dapnet Data Load'

    print_event_time(event)

    dapnet_callsign_data = StringIO(json.dumps(requests.get(dapnet_url, auth=HTTPBasicAuth("n8acl","Xyke8c11qD6I9vTpz63U")).json()))

    dapnet_data = pd.read_json(dapnet_callsign_data)

    dapnet_data.drop('ownerNames', axis=1, inplace=True)

    dapnet_data.to_sql(con=db_engine, name='dapnet_data', if_exists='replace', index=False)
