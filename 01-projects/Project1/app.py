from flask import Flask
from datetime import datetime, date

app = Flask(__name__)

@app.route("/")
def timestamp():
    now = datetime.now() # datetime for the time
    today = date.today() # date for the date

    current_time = now.strftime("%H:%M:%S") 

    return f"Today is {today} and the current time is {current_time}"

# if __name__ == "__main__":
#     app.run(debug=True)