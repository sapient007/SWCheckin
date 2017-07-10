from __future__ import print_function
from swapp.db import DataAccessLayer
from datetime import datetime
from sqlalchemy.sql import select, insert, delete


dal = DataAccessLayer()
db_connection = dal.connect_to_db()


#data access functions
def get_reservation_by_confirmationId(confirmationId):
    reservations_select = select([dal.reservations]).where(
        dal.reservations.c.confirmation_id == confirmationId)
    return db_connection.execute(reservations_select)


def add_reservation(confirmationId, firstName, lastName, flightDateTime):
    ins = insert(dal.reservations).values(
        confirmation_id = confirmationId,
        first_name = firstName,
        last_name = lastName,
        departureDateTime = flightDateTime,
        checkedIn = False
    )
    print(str(ins))
    result = db_connection.execute(ins)
    print(result.rowcount)

def del_reservation(confirmationId):
    if confirmationId is None:
        #nothing happens
        print("nothing happens here")
    elif confirmationId == "All":
        #delete everything from reservations Table
        delete_all = delete(dal.reservations)
        result = db_connection.execute(delete_all)
        print("reservations now has (" + str(result.rowcount) + ") rows")
    else:
        #delete just the confirmationID
        delete_single = delete(dal.reservations).where(reservations.c.confirmation_id == confirmationId)
        result = db_connection.execute(delete_single)
        print("reservations now has (" + str(result.rowcount) + ") rows")



def insert_dummydata():
    del_reservation("All")
    #for count in range(10):
        #add_reservation('{}{}'.format('testconfirmation', str(count)), 'testname', 'testname',  datetime.now())


def main():
    #test my database
    insert_dummydata()
