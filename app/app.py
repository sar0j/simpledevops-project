from flask import Flask
import os
import psycopg2
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "postgres"),
        database=os.environ.get("POSTGRES_DB", "mydb"),
        user=os.environ.get("POSTGRES_USER", "mydbuser"),
        password=os.environ.get("POSTGRES_PASSWORD", "mydbpassword")
    )

@app.route("/")
def home():
    env = os.environ.get("ENV", "unknown")
    app_name = os.environ.get("APP_NAME", "unknown")
    return f"App: {app_name} | ENV: {env} | GitOps with ArgoCD🚀🚀"

@app.route("/users")
def get_users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return {"users": users}

@app.route("/adduser/<name>")
def add_user(name):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": f"User {name} added successfully"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)