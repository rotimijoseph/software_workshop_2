from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def quotes():
    f = open('quotes.txt', 'r')
    read = f.readlines()
    quote = random.choice(read)

    f.close()
    return quote
