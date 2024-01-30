from flask import render_template, request
from app import app
from datetime import datetime, date
import random

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/timestamp")
def timestamp():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")

    return render_template("timestamp.html", current_time=current_time, today=today, time_stamp="Timestamp")

@app.route("/quotes")
def quotes():
    with open('app/data/quotes.txt', 'r') as file:
        read = file.readlines()
        random_quote = random.choice(read)

    return render_template('quotes.html', quote_title="Quote of the Day", content=random_quote)

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