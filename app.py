from flask import Flask
from flask import render_template
app = Flask(__name__)
 
@app.route('/')
def home():
                return render_template("home.html")
               
               
@app.route('/uhart/')
def uhart():
                return render_template("uhart.html")
               
@app.route('/uhart/MATH')
def uhart_math():
                return render_template("uhart_math.html")
               
@app.route('/uhart/<department>/<coursecode>')
def uhart_class(department, coursecode):
                return render_template(
                                "uhart_course.html",
                                department = department,
                                course = coursecode,
                )
               
@app.route('/account/<username>')
def account(username):
                return render_template(
                                "account.html",
                                name = username
                )