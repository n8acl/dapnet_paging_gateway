#############################
##### Import Libraries

import json
import requests
import sys
import os
from requests.auth import HTTPBasicAuth
import http.client, urllib
import mysql.connector
from mysql.connector import Error


#############################
##### Define Variables

# define mysql connection variables
mysql_host = 'MYSQL HOST IP ADDRESS'
mysql_user = 'MYSQL USERNAME'
mysql_password = 'MYSQL PASSWORD'


#############################
##### DO NOT CHANGE BELOW

linefeed = "\r\n"
dapnet_url = 'http://www.hampager.de:8080/calls'
dapnet_data = os.path.dirname(os.path.abspath(__file__)) +  "/dapnet.json"
mysql_databasename = 'dapnet_freepbx' # DO NOT CHANGE THIS

# configure Database connection for MySQL Connector
db_config = {
    'host': mysql_host,
    'database': mysql_databasename,
    'user': mysql_user,
    'password': mysql_password,
    'auth_plugin': 'mysql_native_password'
}

conn = mysql.connector.connect(**db_config)

# Load DAPNET Credentials
df = open(dapnet_data)
creds_data = json.load(df)

#############################
##### Define Functions

def select_sql(conn, sql):
    # Executes SQL for Selects - Returns a "value"
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def exec_sql(conn,sql):
    # Executes SQL for Updates, inserts and deletes - Doesn't return anything
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def send_dapnet(creds, send_to, text):

    data = json.dumps({"text": text, "callSignNames": [send_to], "transmitterGroupNames": [creds["tx_group"]], "emergency": False})
    response = requests.post(dapnet_url, data=data, auth=HTTPBasicAuth(creds["username"],creds["password"])) 


#############################
##### Main Program

# Load paramters to variables
send_to_ric = sys.argv[1]
callback = sys.argv[2]
calling_from = sys.argv[3]

# Get the callsign from the extension calling from
sql = "select callsign from ext_data where extension = '" + calling_from + "';"
results = select_sql(conn,sql)

for row in results:
    from_callsign = row[0]

# Get Callsign to send to from DMR ID
sql = "select callsign from radioid_data where radio_id = " + send_to_ric + ";"
results = select_sql(conn,sql)

for row in results:
    to_callsign = row[0]


# Build Message and then send

send_dapnet(creds_data["my_creds"], to_callsign, from_callsign + ": Call me at " + callback + " #HOIP_DAPNET_GATEWAY")