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
import csv

#############################
# Define the global variables
linefeed = "\r\n"
radioid_dmr_url = 'https://www.radioid.net/static/user.csv' # done

#############################
##### Define Functions

def xstr(s):
    return '' if s is None else str(s)

def print_event_time(event):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(event + " " + current_time)

def data_import(db_engine,pwd):
    event = 'RadioID DMR ID Data Load'

    print_event_time(event)

    users_file = os.path.join(pwd, 'users.csv')

    response = requests.get(radioid_dmr_url, allow_redirects=True)

    open(users_file,'wb').write(response.content)

    radioid_dfs = pd.read_csv(users_file)

    radioid_dfs.to_sql(con=db_engine, name='radioid_data', if_exists='replace', index=False)

    os.remove(users_file)