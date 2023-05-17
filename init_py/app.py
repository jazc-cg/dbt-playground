import time
from datetime import datetime
import random

from sqlalchemy import create_engine

db_name = 'dbtdb'
db_user = 'dbtuser'
db_pass = 'pssd'
db_host = 'localhost'
db_port = '5433'

# Connecto to the database
# ex: 
# default: engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")
# psychopg2: engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")
# engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")
db_string = f"postgresql+pg8000://{db_user}:{db_pass}@{db_host}/{db_name}"
db = create_engine(db_string)

def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    db.execute(f"""
        INSERT INTO orders (id,created_timestamp,product_id) VALUES (
            {n}, {datetime.now()}, {n + 100}
        );
    """)

def init_table():
    query = """
        CREATE TABLE IF NOT EXISTS orders (
            id INT,
            created_timestamp timestamp,
            product_id INT
        );
        CREATE TABLE IF NOT EXISTS products (
            id INT,
            name VARCHAR,
            description VARCHAR,
            created_timestamp timestamp
        );
    """
    result_set = db.execute(query)  

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT id " + \
            "FROM orders " + \
            "WHERE created_timestamp >= (SELECT max(created_timestamp) FROM orders)" +\
            "LIMIT 1"
    
    result_set = db.execute(query)  
    for (r) in result_set:  
        return r[0]

if __name__ == '__main__':
    print('Application started')

    while True:
        add_new_row(random.randint(1,100000))
        print('The last value insterted is: {}'.format(get_last_row()))
        time.sleep(5)