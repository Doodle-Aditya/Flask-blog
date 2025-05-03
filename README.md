
# 📝 Flask Blog Website

A fully functional blog website built using **Flask**, styled with custom CSS, and powered by **PostgreSQL (via Neon)**. The project supports user registration, login, and a blog posting system with clean routing and form handling.

---

## 📁 Project Structure

```
flask_blog_app/
│
├── app.py
├── requirements.txt
│
├── static/
│   └── css/
│       ├── about.css
│       ├── blog.css
│       ├── contact.css
│       ├── login.css
│       ├── register.css
│       └── style.css
│
├── templates/
│   ├── about.html
│   ├── blog.html
│   ├── contact.html
│   ├── index.html
│   ├── login.html
│   └── register.html
```

---

## 🚀 Features

- 🧑‍💻 User Registration and Login (with validation)
- 📬 Contact page (static content)
- 📚 Blog page where users can view and write posts
- 🧾 About page with information
- 🌐 Responsive layout using custom CSS
- 🛡️ CSRF Protection using Flask-WTF
- 💾 PostgreSQL database hosted on [Neon](https://neon.tech)
- 🔒 Secure password hashing with Werkzeug
- 📦 Modular code with Jinja2 templates

---

## 🛠️ Technologies Used

- **Backend**: Flask, Flask-WTF, PostgreSQL
- **Frontend**: HTML5, CSS3, Jinja2
- **Database**: PostgreSQL (via Neon DB)
- **Hosting Ready**: App structure supports deployment on platforms like Railway, Render, etc.

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/doodle-aditya/Flask-blog.git
   cd Flask-blog
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**
   - Create a `.env` file or use your system’s env manager:
     ```
     DATABASE_URL=your_neon_postgres_url
     SECRET_KEY=your_secret_key
     ```

5. **Run the Flask app**
   ```bash
   flask run
   ```

---

## 📌 Pages Overview

| Page       | Route          | Description                           |
|------------|----------------|---------------------------------------|
| Home       | `/`            | Landing page with welcome content     |
| About      | `/about`       | Information about the creator/project |
| Blog       | `/blog`        | Shows posts; form to add new post     |
| Contact    | `/contact`     | Static contact page                   |
| Login      | `/login`       | Login form for registered users       |
| Register   | `/register`    | Sign-up form with validation          |

---


## 🧠 What I Learned

- Connecting Flask apps to cloud PostgreSQL (Neon)
- Form handling and validation with Flask-WTF
- Template inheritance and static file management
- Deployment-ready project structure

---

## 📬 Contact

**Aditya Nishad**  
GitHub: [doodle-aditya](https://github.com/doodle-aditya)  
Email: adityanishad98196@gmail.com

---
