import mysql.connector


def insert_to_table(connector, cursor, table, columns, values):
    '''
    this function assumes user to know what columns are needed, 
    later on i will come back for more
    '''
    # cast all items in values into string XXX
    values = [f'"{v}"' if isinstance(v, str) and v != "Null" else str(v) for v in values]
    # create the insert sql XXX (better to construct the sql with in cursor.execute())
    query_str = f"INSERT INTO {table} ({', '.join(iter(columns))}) VALUES ({', '.join(iter(values))})"
    # print(query_str, end="\r")
    # execute
    try:
        cursor.execute(query_str)
        connector.commit()  # push to the database
    except mysql.connector.Error as err:
        raise err