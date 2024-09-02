# http://127.0.0.1:5000

from flask import Flask

app = Flask(__name__)

# Define a route for the home function
@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO</h1>"

if __name__ == "__main__":
    app.run()
