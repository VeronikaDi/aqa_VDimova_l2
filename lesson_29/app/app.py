import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    "dbname": "mytestdatabase",
    "user": "HomaHum",
    "password": "homarunninghome",
    "host": "db",
    "port": "5432"
}


def connect_db():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn


def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()
    conn.close()


def get_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def update_user(user_id, name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
