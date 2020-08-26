from flask import flask

app = Flask(__name__)

@app.root("/")

def head():
    return "hello world"

if __name__ == "__main__":
    app.run(debug = True)