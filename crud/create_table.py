import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def create_users_table():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()#            # Define the CREATE TABLE query
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) NOT NULL
            );
            """
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            print("Users table created successfully or already exists.")
        except Exception as e:
            print(f"Error creating users table: {e}")
        finally:
            conn.close()

