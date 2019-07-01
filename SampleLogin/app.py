"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import  InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissuppossedtobesecret!'
Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=80)])
    remember = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
     username = StringField('Username', validators=[InputRequired(),Length(min=4, max=15)])
     password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=80)])
     email = StringField('email', validators = [InputRequired(), Email(message='Invalid email'), Length(max=50)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
        form = LoginForm()

        if form.validate_on_submit():
                return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
        
    return render_template('login.html', form=form)

@app.route('/signup' , methods=['GET', 'POST']))
def signup():
        form = RegisterForm()

        if form.validate_on_submit():
                return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data </h1>'
        
    return render_template('signup.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
