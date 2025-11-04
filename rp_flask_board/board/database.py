import psycopg2

def get_pg_db_conn():
    conn = psycopg2.connect(
        host="board-app-psql-db-1",
        database="flask_db",
        user="admin",
        password="P4ssw0rd",
        port="5432"
    )
    return conn
