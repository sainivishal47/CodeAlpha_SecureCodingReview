from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CodeAlpha Secure Coding Review</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f2f2;
                text-align: center;
                padding-top: 80px;
            }

            .box {
                background: white;
                width: 400px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px #aaa;
            }

            input {
                width: 90%;
                padding: 10px;
                margin: 8px;
            }

            button {
                padding: 10px 25px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>CodeAlpha</h1>
            <h2>Secure Coding Review</h2>

            <p>Python Flask Login Demo</p>

            <form method="POST" action="/login">

                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    required
                >

                <br>

                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    required
                >

                <br>

                <button type="submit">Login</button>

            </form>
        </div>
    </body>
    </html>
    """


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if username and password:
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login Result</title>
        </head>

        <body style="font-family: Arial; text-align: center; padding-top: 100px;">

            <h1>Login Request Received</h1>

            <p>Username: {username}</p>

            <p>
                Password was received securely through a POST request.
            </p>

            <p>
                This is a local educational demonstration.
            </p>

            <a href="/">Back to Login</a>

        </body>
        </html>
        """

    return "Invalid input", 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
