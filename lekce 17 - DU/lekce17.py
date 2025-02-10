from flask import Flask, render_template, request, redirect, url_for
from fake_db import users
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("pages/home.html")

@app.route('/about')
def about():
    return render_template("pages/about.html")

@app.route('/users')
def users_list():
    return render_template("pages/users_list.html", users=users)

@app.route('/profile/<int:id>')
def profile(id):
    return render_template("pages/profile.html", user=users[id])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        print(f"EMAIL: {email}")
        print(f"MESSAGE: {message}")
        return redirect(url_for("users_list"))
    else:
        return render_template("pages/contact.html")

if __name__ == '__main__':
    app.run(debug=True)
