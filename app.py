
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")

def hello_earth():
    return "Hello, earth"

if __name__ == "__main__":
    app.run()
