import os
import sys

import sqlalchemy as db
from sqlalchemy import func
# from sqlalchemy import text as sqltext, select, MetaData, Table, Column
from sqlalchemy_utils import database_exists, create_database
import datetime


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
# Define Database Engine

try:
    db_engine = dbc.db_connection()
    print("Database Connection established")
except Exception as e:
    print("Database Connection could not be established.", e)


#############################
##### Define Variables

linefeed = "\r\n"
pwd = os.path.join(os.path.dirname(__file__))

#############################
# create new Database

print("Creating Database....")

create_database(db_engine.url)

metadata = db.MetaData()

print("Creating Tables....")

dapnet_data = db.Table('dapnet_data', metadata,
                db.Column('name',db.String(10)),
                db.Column('description',db.String(500)),
                db.Column('numeric', db.Boolean())
)

radioid_data = db.Table('radioid_data', metadata,
                db.Column('radio_id',db.Integer()),
                db.Column('callsign',db.String(10)),
                db.Column('first_name', db.String(50)),
                db.Column('last_name', db.String(50)),
                db.Column('city', db.String(50)),                
                db.Column('state', db.String(50)),  
                db.Column('country', db.String(50))              

)

ext_data = db.Table('ext_data', metadata,
                db.Column('callsign',db.String(10)),
                db.Column('extension',db.String(12))
)

metadata.create_all(db_engine)

#############################
# create any directories needed for downloads etc.

# Create data directory for file downloads
print("Creating Data Directory....")
data_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(data_dir, exist_ok=True)