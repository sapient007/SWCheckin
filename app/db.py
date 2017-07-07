"""
database class on how to connect to and create schema
"""

import os
import json
import datetime
from sqlalchemy import (
    Table, Column, Integer, Numeric, String, ForeignKey,
    DateTime, Boolean, MetaData, create_engine, insert, select)


class DataAccessLayer:

    # import environment variables from cloud foundry
    local = False
    engine = None
    connection = None
    connection_string = None

    metadata = MetaData()
    reservations = Table('reservations', metadata,
        Column('confirmation_id', String(10), primary_key=True),
        Column('user_id', Integer()),
        Column('departureDateTime', DateTime),
        Column('first_name', String(50), nullable=False),
        Column('last_name', String(50), nullable=False),
        Column('checkedIn', Boolean))

    users = Table('users', metadata,
        Column('user_id', Integer(), primary_key=True),
        Column('username', String(15), nullable=False, unique=True),
        Column('first_name', String(50), nullable=False),
        Column('last_name', String(50), nullable=False),
        Column('password', String(25), nullable=False))

    def find_vcap(self):
        vcap = os.getenv('VCAP_SERVICES')
        if vcap is None:
            #use sqllite
            self.local = True
        else:
            vcap_service = json.loads(vcap)
            pass
            # find what type of service is connected and return tuples of connection info

    # use default values for local database
    def create_db_local(self):
        # self.engine = create_engine('sqlite:///:memory:')
        self.engine = create_engine('sqlite:///whatever.db')
        self.metadata.create_all(self.engine)

    # initate_db based on backend config
    def init_db(self):
        # look for some connection variables.
        if self.local:
            engine = self.create_db_local()
        else:
            self.create_db()

    def connect_to_db(self):
        self.find_vcap()
        if self.engine is None:
            self.init_db()
        #if not self.engine.dialect.has_table(engine, "reservations"):
            #If table doesn't exisit, create them

        self.connection = self.engine.connect()
        return self.connection


dal = DataAccessLayer()
dal.connect_to_db()
