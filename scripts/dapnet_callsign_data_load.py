##### Import Libraries

import json
import pandas as pd
import requests
import sys
import os
from requests.auth import HTTPBasicAuth
import mysql.connector
from mysql.connector import Error
import sqlalchemy
from datetime import datetime, date, time, timedelta


#############################
##### Define Variables

# define mysql connection variables
mysql_host = 'MYSQL HOST IP ADDRESS'
mysql_user = 'MYSQL USERNAME'
mysql_password = 'MYSQL PASSWORD'

#############################
##### DO NOT CHANGE BELOW

linefeed = "\r\n"
dapnet_url = 'http://www.hampager.de:8080/callsigns'
radioid_url = 'https://www.radioid.net/static/user.csv'
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

# configure Database connection for SQL Alchemy
db_conn = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(mysql_user, mysql_password, 
                                                      mysql_host, mysql_databasename))


#############################
##### Define Functions
   
def select_sql(conn, sql):
    # Executes SQL for Selects - Returns a "value"
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall(), cur.rowcount

def exec_sql(conn,sql):
    # Executes SQL for Updates, inserts and deletes - Doesn't return anything
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

#############################
##### Main Program

now = datetime.now()
current_time = now.strftime("%H:%M")

## First, lets insert the DAPNET Callsign List

print("Loading DAPNET Callsign Data " + current_time)

sql = "drop table if exists dapnet_data;"

exec_sql(conn,sql)

sql = "create table dapnet_data (callsign text);"

exec_sql(conn,sql)

dapnet_callsign_data = requests.get(dapnet_url, auth=HTTPBasicAuth(<your-username>,<your_password>)).json() 

for i in range(0,len(dapnet_callsign_data)):
    sql = "insert into dapnet_data(callsign) "
    sql = sql + "values('" + dapnet_callsign_data[i]['name'] + "');"

    exec_sql(conn,sql)

## Now let's get the Radio ID data for the DMR IDs

now = datetime.now()
current_time = now.strftime("%H:%M")

print("Loading RadioID Data " + current_time)

response = requests.get(radioid_url, allow_redirects=True)

open('users.csv','wb').write(response.content)

radioid_dfs = pd.read_csv('users.csv')

radioid_dfs.to_sql(con=db_conn, name='radioid_data', if_exists='replace')

os.remove('users.csv')

## Now let's clean up the Radio ID Data to only include those callsigns that have a DAPNET account.
## This is just to keep the data smaller.

sql = "delete from radioid_data where callsign not in (select upper(callsign) as callsign from dapnet_data)"
exec_sql(conn,sql)

print("Completed: " + current_time)