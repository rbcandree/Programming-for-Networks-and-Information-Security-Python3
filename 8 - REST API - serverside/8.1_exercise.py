"""
In this exercise we'll be building an API for simplified inventory management. 
API is used by a store that buys and sells books. Your job is to build an API that keeps track of the books currently in the inventory.

You are expected to use Flask for the interface implementation and postgresql as your database backbone. 
That is, when an item is sold to your shop you should insert it into the database and when one is purchased you should delete the purchased object from the database.

In each of the steps you should also implement a test program to test your interface. This should only be a couple of lines of code. 
Example (notice how we include a json in the POST):

import requests

rreply = requests.post('http://localhost:5000/sell/', json={"title": "book","author":"Esteri","year_of_publication":1990})
print(rreply.status_code)
print(rreply.json())

1. Implement the route:
/sell/

This route is accessed via POST method. The data is delivered in a JSON.
When the interface gets a "sell request", it should insert the item into the database. 
The items should have the following information: Title, Author, Year of Publication. For this we will obviously need a database table.
An id is added to each individual book by the system (might be good to use the serial datatype in the database for this). 
This id is shown in the response from the /list/ route and it is referenced by the /purchase/ route.

2. Implement the route:
/list/
This route is accessed via GET method only. It returns a list of the items currently in the inventory.

3. Implement the route:
/purchase/<item id>
This route is accessed via GET method. The route checks if the item referenced by the <item id> is in the inventory. 
If the item is in the inventory it is removed from there and an 'ok' -response is sent to the client. 
If there are no items with <item id> in the inventory a 'not found' response is sent to the client.
"""
import psycopg2, flask
from flask import request

inventory = {}

def create_db_table():
    commands = ("""DROP TABLE IF EXISTS bookstore""","""CREATE TABLE bookstore (id SERIAL PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), publication_year INTEGER)""")
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="your_database_name", user="your_username", password="your_password")
        db_cursor = conn.cursor()
        for command in commands:
            print("Executing SQL query: " + command)
            db_cursor.execute(command)  # execute DROP & CREATE TABLE
        conn.commit()                   # commit the changes to the database
        db_cursor.close()               # close communication with the PSQL database server
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()                # terminate connection with the PSQL database server

def insert_data(data_list):
    sql_query1 = """INSERT INTO bookstore (title, author, publication_year) VALUES(%s, %s, %s);"""
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="your_database_name", user="your_username", password="your_password")
        db_cursor = conn.cursor()
        print("Executing: " + sql_query1)
        db_cursor.execute(sql_query1, data_list)
        conn.commit()
        db_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

app = flask.Flask(__name__)
@app.route('/sell/', methods=['POST'])
def api_request_sell():
    print(request.json)
    data = request.json
    data_for_db = [request.json["title"], request.json["author"], int(request.json["publication_year"])]
    insert_data(data_for_db)
    return f"Your request: {str(data)}\n"

@app.route('/list/', methods=['GET'])
def api_request_list():
    global inventory
    sql_query2 = """SELECT * FROM bookstore;"""
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="your_database_name", user="your_username", password="your_password")
        db_cursor = conn.cursor()
        print("Executing: " + sql_query2)
        db_cursor.execute(sql_query2)
        db_list = db_cursor.fetchall()
        db_cursor.close()
    except (Exception, psycopg2.DatabaseError) as exc:
        print(exc)
    finally:
        if conn is not None:
            conn.close()
    reply = {} 
    for _id, _title, _author, _publication_year in db_list:
        reply.setdefault(_id, []).append(_title)
        reply.setdefault(_id, []).append(_author)
        reply.setdefault(_id, []).append(_publication_year)
    inventory = reply
    #inventory = reply.copy()
    return f"Available books: {str(reply)}\n"
    #return jsonify(reply)

@app.route('/purchase/<item_id>/', methods=['GET'])
def api_request_purchase(item_id):
    global inventory
    if int(item_id) not in inventory.keys():
        return "Not found\n"
    else:
        sql_query3 = """DELETE FROM bookstore WHERE id=%s;"""
        conn = None
        try:
            conn = psycopg2.connect(host="localhost", database="your_database_name", user="your_username", password="your_password")
            db_cursor = conn.cursor()
            print("Executing: " + sql_query3)
            db_cursor.execute(sql_query3, item_id)
            conn.commit()
            db_cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return "OK\n"

if __name__ == '__main__':
    create_db_table()
    app.run()