import os
import mysql.connector as connection
import pandas as pd
import streamlit as st


@st.experimental_singleton
def init_connection():
    db_connection=connection.connect(host="dbm2.its.virginia.edu",
                               user=os.environ['database_user'],
                               password=os.environ['database_password'],
                               database="civeleklab_SMC")
    return db_connection

