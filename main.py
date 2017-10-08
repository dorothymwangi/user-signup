from flask import Flask, request,redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template('signup_form.html')


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']
    username_error =''
    password_error =''
    verify_error =''
    email_error =''

    if len(username) <3 or len(username) >20 or " " in username:
            username_error = "Username length out of range(3-20)"

    if len(password) <3 or len(password) >20 or " " in password:
            password_error = 'Password length out of range(3-20)'
            password =''

    if verify_password == "":
        verify_error ='Invalid verification'

    elif password !=verify_password:
        verify_error ='Does not match password'
        verify_password ='' 

    if email !='' and len(email) <3 or len(email)>20:
        email_error = "Email length out of range(3-20)"

    elif email !='' and ("@" not in email) or ("." not in email):
        email_error = "Invalid email"

    if not username_error and not password_error and not verify_error and not email_error:
       return render_template('welcome.html', username=username)

    else:
        return render_template('signup_form.html', username=username, email=email, username_error=username_error,
        password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()