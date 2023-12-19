import psycopg2

def create_tables():
    commands = (
        """
        DROP TABLE IF EXISTS table_1
        """,
        """
        CREATE TABLE table_1 (
            id INTEGER PRIMARY KEY,
            last_name VARCHAR(255),
            year_of_birth INTEGER,
            time_of_purchase TIMESTAMP
        )
        """)
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="your_database_name",
            user="your_username",
            password="your_password"
        )
        db_cursor = conn.cursor()

        for command in commands:
            print("Executing SQL query: " + command)
            db_cursor.execute(command)
        # close communication with the PostgreSQL database server
        db_cursor.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_data():
    """ insert from data.txt into the table_1 table  """
    sql_query = """INSERT INTO table_1 (id, last_name, year_of_birth, time_of_purchase) VALUES(%s, %s, %s, %s);"""
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="your_database_name",
            user="your_username",
            password="your_password"
        )
        db_cursor = conn.cursor()

        with open("/home/path_to_the_file/data.txt", "r") as data:
            next(data) # to skip the header
            for datarow in data:
                datarow_as_list = datarow.split(";")
                #datarow_as_list = datarow.strip().split(";")
                if not datarow_as_list[0].isalpha():
                    db_cursor.execute(sql_query, datarow_as_list)

        conn.commit()
        db_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
    insert_data()