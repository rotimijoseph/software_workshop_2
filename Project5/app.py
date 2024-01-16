from flask import Flask, Request
from datetime import datetime, date
import random

app = Flask(__name__)

# Write an app that combines all the above apps with a navigation bar that can switch between all the pages.

@app.route("/")
def homepage():
    return "<h1> Welcome to this really simple app.</h1>"

@app.route("/timestamp")
def timestamp():
    now = datetime.now() # datetime for the time
    today = date.today() # date for the date

    current_time = now.strftime("%H:%M:%S") 

    return f"Today is {today} and the current time is {current_time}"

@app.route("/quotes")
def quotes():
    f = open('quotes.txt', 'r')
    read = f.readlines()
    quote = random.choice(read)

    f.close()
    return quote

@app.route("/<int:num>")
    
def find_prime_factors(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1

    all_factors = " ".join(str(num) for num in factors)
    return f"The factors are: {all_factors}"

@app.route("/app")
def app_obj():
    return str(app.__dict__)

@app.route("/request")
def req_obj():
    return str(Request.__dict__)
