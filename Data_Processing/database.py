import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
#load_dotenv()

def connect_to_database(host, user, password, database=None):
    """Connect to a MySQL database."""
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def create_database(cursor, db_name):
    """Drop the database if it exists and create a new one."""
    cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cursor.execute(f"CREATE DATABASE {db_name}")
