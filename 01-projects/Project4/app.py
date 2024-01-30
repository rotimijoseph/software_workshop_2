from flask import Flask, Request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/app")
def app_obj():
    return render_template('app.html', obj_name="App Object", info=dir(app))

@app.route("/request")
def req_obj():
    return render_template('app.html', obj_name="Request Object", info=dir(Request))

