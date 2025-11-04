import os
import psycopg2
from flask import current_app

# Koneksi ke PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="admin",
    password="P4ssw0rd",
    port="5432"
)

cur = conn.cursor()

# Hapus tabel jika sudah ada
cur.execute("DROP TABLE IF EXISTS post;")

# Buat tabel baru
cur.execute("""
    CREATE TABLE post (
        id SERIAL PRIMARY KEY,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        author TEXT NOT NULL,
        message TEXT NOT NULL
    );
""")

# Simpan perubahan
conn.commit()

# Tutup koneksi
cur.close()
conn.close()
