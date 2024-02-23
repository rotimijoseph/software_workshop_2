from flask import render_template, redirect, url_for, flash
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alevels")
def alevels():
    
    predicted_grades = str(input())
    
    grades = []
    for char in predicted_grades:
        if char == "ACBDEFGU":
            grades.append(char)
    
        if grades == ["A", "A", "A"]:
            return "You can study Computer Science, congratulations!"
        else:
            return "Need to get those grades up hun"
    
    return render_template("alevels.html")