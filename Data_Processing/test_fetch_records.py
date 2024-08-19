import sys
import pandas as pd
from database import connect_to_database
from IPython.display import display 
from dotenv import load_dotenv
import os
load_dotenv()

def fetch_records(cursor, table_name):
    """Fetch 5 records from the specified table and return as a DataFrame."""
    query = f"SELECT * FROM {table_name} LIMIT 5;"
    cursor.execute(query)
    records = cursor.fetchall()
    
    # Get the column names from the cursor description
    columns = [desc[0] for desc in cursor.description]
    
    # Create a DataFrame from the records and columns
    df = pd.DataFrame(records, columns=columns)
    
    return df

def main(database_name):
    try:
        # Connect to the database using the user-provided name
        conn = connect_to_database(
            host="127.0.0.1", 
            user="root", 
            password=os.getenv("password"), 
            database=database_name
        )
        cur = conn.cursor()

        # Define table names
        tables = ["Customer", "EcommerceWebsite", "Product", "Orders", "Payment"]

        # Fetch and display 5 records from each table in a tabular format
        for table in tables:
            print(f"Fetching records from {table} table:")
            df = fetch_records(cur, table)
            display(df)  # Use display() to show the DataFrame as a table
            print("\n")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a database name.")

