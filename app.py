from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
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

# Forms
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

class SearchForm(FlaskForm):
    key_word = StringField('Blog Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class BlogForm(FlaskForm):
    blogname = StringField('Blog Name', validators=[DataRequired()])
    description = TextAreaField('Short Description', validators=[DataRequired()])
    fullblog = TextAreaField('Full Blog', validators=[DataRequired()])
    submit = SubmitField('Add Blog')

# Routes
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

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_1 (user_name, name_of_user, email, pass) VALUES (%s, %s, %s, %s)", 
                       (user_name, name, email, password))
        mysql.connection.commit()
        cursor.close()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

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

        if user and user[3] == password:
            session['user_name'] = user_name
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid Username or Password', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_name', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    search_form = SearchForm()
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        blogname = blog_form.blogname.data
        description = blog_form.description.data
        fullblog = blog_form.fullblog.data

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO blogs (blogname, description, fullblog) VALUES (%s, %s, %s)', 
                       (blogname, description, fullblog))
        mysql.connection.commit()
        cursor.close()

        flash("Blog added successfully!", "success")
        return redirect(url_for('blog'))

    results = None
    if search_form.validate_on_submit():
        key_word = search_form.key_word.data
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM blogs WHERE blogname LIKE %s", ('%' + key_word + '%',))
        results = cursor.fetchall()
        cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM blogs")
    all_blogs = cursor.fetchall()
    cursor.close()

    return render_template('blog.html', search_form=search_form, blog_form=blog_form, results=results, all_blogs=all_blogs)

if __name__ == '__main__':
    app.run(debug=True)
