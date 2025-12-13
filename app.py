from flask import Flask, request, redirect, render_template, session, url_for
import manager_utils
import os

# -----------------------------
# Create Flask app
# -----------------------------
app = Flask(__name__)
app.secret_key = os.urandom(24)  # required for session

# -----------------------------
# Routes
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        master = request.form["master"]
        try:
            manager_utils.register_user(username, master)
            message = "User registered successfully! Login now."
        except Exception as e:
            message = str(e)
    return render_template("register.html", message=message)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        master = request.form["master"]
        if manager_utils.check_login(username, master):
            session["user"] = username
            session["master"] = master
            return redirect(url_for("dashboard"))
        else:
            message = "Invalid username or master password!"
    return render_template("login.html", message=message)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", message="", session=session)

@app.route("/add", methods=["POST"])
def add_password():
    if "user" not in session:
        return redirect(url_for("login"))
    manager_utils.add_password(
        session["user"],
        session["master"],
        request.form["service"],
        request.form["username_pw"],
        request.form["password"]
    )
    return render_template("dashboard.html", message="Password added ✅", session=session)

@app.route("/view", methods=["POST"])
def view_password():
    if "user" not in session:
        return redirect(url_for("login"))
    try:
        pw = manager_utils.get_password(session["user"], session["master"], request.form["service"])
        message = f"Password for {request.form['service']}: {pw}"
    except Exception as e:
        message = str(e)
    return render_template("dashboard.html", message=message, session=session)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -----------------------------
# Run locally
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)



