import os
import mysql.connector as connection
import pandas as pd


db_connection=connection.connect(host="dbm2.its.virginia.edu",
                           user=os.environ['database_user'],
                           password=os.environ['database_password'],
                           database="civeleklab_SMC")

def execute_sql(sql):
    df = pd.read_sql(sql, con=db_connection)
    return df



