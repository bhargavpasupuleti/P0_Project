def create_table(cursor, create_table_sql):
    """Create a table based on the provided SQL statement."""
    cursor.execute(create_table_sql)

def insert_data(cursor, insert_query, data):
    """Insert data into a table based on the provided SQL query."""
    cursor.executemany(insert_query, data)

