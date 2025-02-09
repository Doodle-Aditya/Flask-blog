from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_mysqldb import MySQL

app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = 'A2Z123'

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'userbase'

mysql = MySQL(app)

class RegisterForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    # Custom validation for username
    def validate_user_name(self, field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_1 WHERE user_name = %s", (field.data,))
        existing_user = cursor.fetchone()
        cursor.close()

        if existing_user:
            raise ValidationError("Username is already taken. Please choose another.")

    # Custom validation for email
    def validate_email(self, field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_1 WHERE email = %s", (field.data,))
        existing_email = cursor.fetchone()
        cursor.close()

        if existing_email:
            raise ValidationError("Email is already registered. Please use another email.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        user_name = form.user_name.data
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Store data in MySQL
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_1 (user_name, name_of_user, email, pass) VALUES (%s, %s, %s, %s)",
                       (user_name, name, email, password))
        mysql.connection.commit()
        cursor.close()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

