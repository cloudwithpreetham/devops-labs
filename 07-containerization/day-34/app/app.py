from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "devopsdb")
DB_USER = os.getenv("DB_USER", "devops")
DB_PASSWORD = os.getenv("DB_PASSWORD", "devopspass")
REDIS_HOST = os.getenv("REDIS_HOST", "cache")

@app.route("/")
def home():
    db_status = "Database connection failed"
    cache_status = "Redis connection failed"

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        db_status = "Database connected successfully"
    except Exception as e:
        db_status = f"Database error: {str(e)}"

    try:
        r = redis.Redis(host=REDIS_HOST, port=6379)
        r.ping()
        cache_status = "Redis cache connected successfully"
    except Exception as e:
        cache_status = f"Redis error: {str(e)}"

    return f"""
    <h1>Updated Day 34 Multi-Container App</h1>
    <p>{db_status}</p>
    <p>{cache_status}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
