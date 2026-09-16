from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("users.db")

    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

    result = conn.execute(query).fetchone()

    if result:
        return "Login successful"

    return "Invalid login"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
