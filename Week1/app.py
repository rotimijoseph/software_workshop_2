from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, you've finally got this stupid thing working, congratulations!"

if __name__ == "__main__":
    app.run(debug=True)