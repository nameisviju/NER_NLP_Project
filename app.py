

from flask import Flask, render_template,request,redirect,session
import api
from db import Database
app = Flask(__name__)

dbo=Database()
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message='Registration successful kindly login to proceed')
    else:
        return render_template('register.html', message='Email is already exists')

    return name + " " + email + " " + password
@app.route("/perform_login",methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response=dbo.search(email,password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email or password')
@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/NER')
def ner():
    return render_template("ner.html")


@app.route('/perform_ner',methods=['post'])
def perform_ner():
       text=request.form.get("ner_text")
       response=api.ner(text)
       print(response)
       return render_template('ner.html',response=response)


app.run(debug=True)

