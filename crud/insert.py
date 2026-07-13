# crud/create.py
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def create_user(user_id, username):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (id, username) VALUES (%s, %s);"
            cursor.execute(query, (user_id, username))
            conn.commit()
            cursor.close()
            print(f"User {username} created successfully.")
        except Exception as e:
            print(f"Error creating user: {e}")
        finally:
            conn.close()

