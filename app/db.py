#database scripts on how to connect to and create schema

import os
import json
import datetime
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime, Boolean, MetaData, create_engine, insert, select

#import environment variables from cloud foundry
def find_vcap():
    vcap = json.loads(os.environ['VCAP_SERVICES'])
    if vcap is none:
        #use sqllite
    else:
        #find what type of service is connected and return tuples of connection info


#use default values for local database
def create_db_local():
    engine = create_engine('sqlite:///:memory:')
    metadata = tables()
    metadata.create_all(engine)

#open connection to PCF services
def create_db():
    

#define table schema
def tables():
    metadata = MetaData()
    reservations = Table('reservations', metadata,
            Column('confirmation_id', String(10), primary_key=true),
            Column('user_id', Integer(), nullable=False)
            Column('departureDateTime', DateTime),
            Column('checkedIn', Boolean))

    users = Table('users', metadata,
        Column('user_id', Integer(), primary_key=True),
        Column('username', String(15), nullable=False, unique=True),
        Column('first_name', String(50), nullable=False),
        Column('last_name', String(50), nullable=False),
        Column('password', String(25), nullable=False))

    return metadata

#initate_db based on backend config
def initate_db():
    #test to see if the table of reservations and users exist. if not, create tables
