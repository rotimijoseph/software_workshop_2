from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import RegistrationForm, BorrowForm, AddStudentForm
from app.models import Student, Loan
from datetime import datetime

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        if not form.validate_dob(form.dob):
            flash('Please enter a valid date of birth.')
            return render_template('registration.html', title="Register", form=form)
        
        flash(f'Registration for {form.username.data} received', 'success')
        return redirect(url_for('index'))
    return render_template('registration.html', title="Register", form=form)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    if form.validate_on_submit():
        new_student = Student(username=form.username.data, firstname=form.firstname.data,
                              lastname=form.lastname.data, email=form.email.data)
        db.session.add(new_student)
        try:
            db.session.commit()
            flash(f'New Student added: {form.username.data} received', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            if Student.query.filter_by(username=form.username.data).first():
                form.username.errors.append('This username is already taken. Please choose another')
            if Student.query.filter_by(email=form.email.data).first():
                form.email.errors.append('This email address is already registered. Please choose another')
    return render_template('add_student.html', title='Add Student', form=form)

@app.route("/borrow", methods=["GET", "POST"])
def borrow():
    form = BorrowForm()
    if form.validate_on_submit():
        # check if student has already taken out a loan
        existing_loan = Loan.query.filter_by(student_id=form.student_id.data, returndatetime=None).first()
        if existing_loan:
            flash('You already have a device on loan. Please return it before borrowing another device.') # flash shows at top of page
            
        # check if student is registered 
        elif not Student.query.filter(Student.student_id == form.student_id.data).first():
            form.student_id.errors.append("Student is not registered.") # with this append method it shows next to the form
            
        # check if item is already being loaned 
        elif Loan.query.filter(Loan.device_id == form.device_id.data).first():
            form.device_id.errors.append("Device is already out for loan.")
        
        # if everything is okay then new loan added to database 
        else:
            new_loan = Loan(student_id=form.student_id.data, device_id=form.device_id.data, borrowdatetime=datetime.now())   
            db.session.add(new_loan)
            try:
                db.session.commit()
                flash(f'You have succesfully loaned this device.')
                return redirect(url_for('index'))
            except:
                db.session.rollback()
                if Loan.query.filter_by(student_id=form.student_id.data, returndatetime=None).first():
                    form.student_id.errors.append('You already have a device on loan. Please return it before borrowing another device.')
    return render_template("borrow.html", form=form)