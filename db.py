import psycopg2
from psycopg2 import sql, OperationalError
import psycopg2.extras
import os
from dotenv import load_dotenv
load_dotenv()
conn=None
#function to connect to database
def get_db_connection():
    try:
        conn=psycopg2.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')

        )
        print("Connection to PostgreSQL DB successful")
        return conn
        

    except OperationalError as e:
        print(f"The error {e} occurred")
        return None

    # finally:
    #     if connection is not None:
    #         connection.close()


conn = get_db_connection()