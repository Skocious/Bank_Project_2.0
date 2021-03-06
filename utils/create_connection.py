import os  # environment variables
from psycopg import connect, OperationalError


def create_connection():
    try:

        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )

        return conn
    except OperationalError:
        return "Could not connect!"


connection = create_connection()


