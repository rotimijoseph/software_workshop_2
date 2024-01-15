from flask import Flask
from datetime import datetime 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, you've finally got this stupid thing working, congratulations!"

@app.route("/time") # need to show the date too 
def timestamp():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Current Time = {current_time}"

if __name__ == "__main__":
    app.run(debug=True)