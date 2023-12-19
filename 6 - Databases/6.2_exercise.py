import psycopg2
import random

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
            time_of_purchase INTEGER
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
    """ insert from data_list into the table_1 table  """
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
        
        last_names = ["Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä", "Hämäläinen", "Laine", "Heikkinen", "Koskinen", "Järvinen", "Lehtonen",
               "Lehtinen", "Saarinen", "Salminen", "Heinonen", "Niemi", "Heikkilä", "Kinnunen", "Salonen", "Turunen", "Salo", "Laitinen",
                 "Rantanen", "Tuominen", "Karjalainen", "Jokinen", "Mattila", "Savolainen", "Lahtinen", "Ahonen"]

        data_list = [[]]
        for num in range(1, 10001):
            data_list.append([])
            data_list[num].append(num)
            data_list[num].append(random.choice(last_names))
            data_list[num].append(random.randint(1970, 2005))
            data_list[num].append(random.randint(1655000000, 1699600000))
        del data_list[0]
        # execute all the INSERT statements
        db_cursor.executemany(sql_query, data_list)

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