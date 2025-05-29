#############################
##### Import Libraries

import json
import sys
import os
from os import system
import requests
from requests.auth import HTTPBasicAuth
import http.client, urllib
import sqlalchemy
from sqlalchemy import text as sqltext, select, MetaData, Table

if os.path.exists('src'):
   # Import our Custom Libraries
   import src.db_functions as dbf
   import src.db_conn as dbc

else:
	#set the parent directory one level up and then import the src files
   current_dir = os.path.dirname(os.path.abspath(__file__))
   parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
   sys.path.insert(0, parent_dir)  

   import src.db_functions as dbf
   import src.db_conn as dbc


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
dapnet_url = 'http://www.hampager.de:8080/calls'


#############################
##### Define Functions

def send_dapnet(creds, send_to, text):

    data = json.dumps({"text": text, "callSignNames": [send_to], "transmitterGroupNames": [creds["tx_group"]], "emergency": False})
    response = requests.post(dapnet_url, data=data, auth=HTTPBasicAuth(creds["username"],creds["password"])) 


#############################
##### Main Program

# Load command line paramters to variables
send_to_ric = sys.argv[1]
callback = sys.argv[2]
calling_from = sys.argv[3]

# Get Callsign to send to from DMR ID
sql = sqlalchemy.select(radioid_data.c.CALLSIGN).where((radioid_data.c.RADIO_ID == send_to_ric))
results = dbf.select_sql(db_engine,sql)

for row in results:
    to_callsign = row[0]

# Get the callsign sending the message from

if cfg["gateway_mode"] == 1:
    from_callsign = cfg["dapnet"]["username"].upper()
else:
    sql = sqlalchemy.select(ext_data.c.callsign).where((ext_data.c.extension == calling_from))
    results = dbf.select_sql(db_engine,sql)

    for row in results:
        from_callsign = row[0].upper()


# Build Message and then send
send_dapnet(cfg["dapnet"], to_callsign, from_callsign + ": Call me at " + callback)