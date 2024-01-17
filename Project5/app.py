from flask import Flask, Request, render_template, request
from datetime import datetime, date
import random

app = Flask(__name__)

# Write an app that combines all the above apps with a navigation bar that can switch between all the pages.

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/timestamp")
def timestamp():
    now = datetime.now() # datetime for the time
    today = date.today() # date for the date
    current_time = now.strftime("%H:%M:%S")

    return render_template("timestamp.html", current_time=current_time, today=today, time_stamp="Timestamp")

@app.route("/quotes")
def quotes():
    f = open('quotes.txt', 'r')
    read = f.readlines()
    random_quote = random.choice(read)
    f.close()

    return render_template('quotes.html', quote_title="Quote of the Day", content=random_quote)

# @app.route("/<int:num>")
# def find_prime_factors(num):
#     factors = []
#     divisor = 2

#     while divisor <= num:
#         if num % divisor == 0:
#             factors.append(divisor)
#             num = num / divisor
#         else:
#             divisor += 1

#     all_factors = " ".join(str(num) for num in factors)
#     return f"The factors are: {all_factors}"

@app.route('/find_prime_factors', methods=['GET', 'POST'])
def find_prime_factors():
    factors = []

    if request.method == 'POST':
        num = int(request.form['number'])
        divisor = 2

        while divisor <= num:
            if num % divisor == 0:
                factors.append(divisor)
                num = num / divisor
            else:
                divisor += 1

    all_factors = " ".join(str(num) for num in factors)
    return render_template('primefactors.html', factors=all_factors, prime_factors= "Prime Factors")

@app.route("/app")
def app_obj():
    return render_template('app.html', obj_name="App Object", info=dir(app))

@app.route("/request")
def req_obj():
    return render_template('app.html', obj_name="Request Object", info=dir(Request))
