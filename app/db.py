#database scripts on how to connect to and create schema

import os
import json
import datetime
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime, Boolean, MetaData, create_engine, insert, select


class DataAccessLayer:

    #import environment variables from cloud foundry
    local = None
    engine = None
    connection = None
    connection_string = None
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




    #initate_db based on backend config
    def initate_db(self, conn_string):
        #look for some connection variables.
        if local is none:
            engine = create_db_local()
        else
            engine = create_db()

    def connect_to_db():
        if not engine.dialect.has_table(engine, "reservations"):
            #If table doesn't exisit, create them
            initate_db()
        connection = engine.connect()
        return connection


dal = DataAccessLayer()
