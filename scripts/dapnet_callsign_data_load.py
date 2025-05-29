##### Import Libraries

import json
import pandas as pd
import sys
import os
from os import system
import requests
from requests.auth import HTTPBasicAuth
import sqlalchemy
from sqlalchemy import text as sqltext, select, MetaData, Table
from datetime import datetime, date, time, timedelta

if os.path.exists('src'):
   # Import our Custom Libraries
   import src.db_functions as dbf
   import src.db_conn as dbc
   import src.dapnet_import as dapnet
   import src.radioid_dmr_import as radioiddmr

else:
	#set the parent directory one level up and then import the src files
   current_dir = os.path.dirname(os.path.abspath(__file__))
   parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
   sys.path.insert(0, parent_dir)  

   import src.db_functions as dbf
   import src.db_conn as dbc
   import src.dapnet_import as dapnet 
   import src.radioid_dmr_import as radioiddmr

#############################
# set database connection

try:
    db_engine = dbc.db_connection()
    print("Database Connection established")
except Exception as e:
    print("Database Connection could not be established.", e)

metadata = sqlalchemy.MetaData()
metadata.reflect(bind=db_engine)

dapnet_data = metadata.tables['dapnet_data']
radioid_data = metadata.tables['radioid_data']
ext_data = metadata.tables['ext_data']


#############################
# import config json file

config_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'config.json'))

with open(config_file, "r") as read_file:
    cfg = json.load(read_file)
read_file.close()

#############################
##### Define Variables

linefeed = "\r\n"
pwd = os.path.join(os.path.dirname(__file__), 'data')

#############################
##### Define Functions
   
def print_event_time(event):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(event + " " + current_time)

#############################
##### Main Program

print_event_time("Data Load Start")

## First, lets insert the DAPNET Callsign List
## uses src.dapnet_import.py

dapnet.data_import(db_engine,pwd)

## Now let's get the Radio ID data for the DMR IDs
## uses src.radioid_dmr_import.py

radioiddmr.data_import(db_engine,pwd)

## Now let's clean up the Radio ID Data to only include those callsigns that have a DAPNET account.
## This is just to keep the data smaller.

subquery = sqlalchemy.select(dapnet_data.c.name)
sql = sqlalchemy.delete(radioid_data).where(~radioid_data.c.callsign.in_(subquery))
dbf.exec_sql(db_engine,sql)

print_event_time("Completed")