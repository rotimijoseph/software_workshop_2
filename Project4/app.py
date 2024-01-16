from flask import Flask 

app = Flask(__name__)

# Write an app that shows values from the App object on one page and the Request object on another
@app.route("/app")
def app_obj():
    return dir(app)

@app.route("/request")
def req_obj():
    return 