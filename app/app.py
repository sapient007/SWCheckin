from app.db import DataAccessLayer
from sqlalchemy.sql import (
    select, insert)

dal = DataAccessLayer()
db_connection = dal.connect_to_db()

#data access functions
def get_reservation_by_confirmationId(confirmationId):
    reservations_select = select([dal.reservations]).where(dal.reservations.c.confirmation_id == confirmationId)
    return db_connection.execute(reservations_select)

def add_reservation(confirmationId, firstName, lastName, flightDateTime):
    ins = insert(dal.reservations).values(
        confirmation_id = confirmationId,
        first_name = firstName,
        lastName = lastName,
        departureDateTime = flightDateTime,
        checkedIn = False
    )
    print (str(ins))
