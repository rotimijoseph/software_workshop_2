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

        if not form.validate_dob(form.dob):
            flash('Please enter a valid date of birth.')
            return render_template('forms.html', title="Register", form=form)
        
        flash(f'Success. Login for {form.username.data}')
        return redirect(url_for('index'))
    return render_template('forms.html', title="Register", form=form)