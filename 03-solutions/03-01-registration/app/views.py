from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import RegistrationForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Login for {form.username.data}')
        return redirect(url_for('index')) # change to like a welcome page I think 
    return render_template('forms.html', title="Register", form=form)