from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = 'A2Z123'
csrf = CSRFProtect(app)

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'userbase'

mysql = MySQL(app)

class RegisterForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

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
        return redirect(url_for('login'))  # Redirect to login page after registration

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()


    if form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_1 WHERE user_name = %s', (user_name,))
        user = cursor.fetchone()
        cursor.close()


        if user:
            db_password = user[3]
            if db_password == password:
                session['user_name'] = user_name

                flash('Login successful!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid Username or Password', 'danger')
        else:
            flash('User not found', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)