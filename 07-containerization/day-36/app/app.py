import os
import time
import psycopg2
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "notesdb")
DB_USER = os.getenv("DB_USER", "notesuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "notespass")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def init_db():
    retries = 10

    while retries > 0:
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL
                );
            """)

            conn.commit()
            cur.close()
            conn.close()
            print("Database initialized successfully")
            break

        except Exception as error:
            print(f"Database not ready yet: {error}")
            retries -= 1
            time.sleep(3)


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":
        note = request.form.get("note")

        if note:
            cur.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
            conn.commit()

        cur.close()
        conn.close()
        return redirect("/")

    cur.execute("SELECT id, content FROM notes ORDER BY id DESC")
    notes = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
