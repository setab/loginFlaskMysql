# app.py

from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import get_all_users, get_user_by_credentials, insert_user, get_all_personal
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    if request.method == "GET":
        user = get_all_personal()
    return render_template("home.html", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_user_by_credentials(username, password)

        if user:
            session["user"] = user[1]
            session["email"] = user[3]
            session["age"] = user[4]
            session["info"] = user[5]
            session["role"] = user[6]

            if session["role"] == "user":
                return redirect(url_for("user_page"))
            else:
                return redirect(url_for("admin"))
        else:
            flash("Invalid Credentials. Please try again.")
            return render_template("login.html")
    else:
        if "user" in session:
            return redirect(url_for("user_page"))
        return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        newUserName = request.form["new-username"]
        newPassword = request.form["new-password"]
        age = request.form["new-age"]
        email = request.form["new-email"]
        personalInfo = request.form["new-personal"]

        if insert_user(newUserName, newPassword, age, email, personalInfo):
            return "Sign up successful"
        else:
            print("Failed to sign up")

    return render_template("signup.html")


@app.route("/user", methods=["GET"])
def user_page():
    if "user" in session:
        username = session["user"]
        email = session["email"]
        age = session["age"]
        info = session["info"]
        role = session["role"]
        return render_template(
            "user.html", username=username, email=email, age=age, info=info, role=role
        )
    else:
        return redirect(url_for("login"))


@app.route("/userposts", methods=["POST", "GET"])
def user_posts():
    if "user" in session:
        info = session["info"]
        return render_template("user_posts.html", about=info)


@app.route("/admin", methods=["GET"])
def admin():
    if "user" in session and session["role"] == "admin":
        all_users = get_all_users()  # Fetch all users for admin view
        return render_template(
            "admin.html",
            username=session["user"],
            email=session["email"],
            age=session["age"],
            info=session["info"],
            role=session["role"],
            all_users=all_users,  # Pass all users to the template
        )
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove user from session
    return redirect(url_for("login"))  # Redirect to login page


if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
