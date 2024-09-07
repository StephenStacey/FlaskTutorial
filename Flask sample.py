# Import necessary modules from the Flask framework
# Flask: The main class for creating a web application
# redirect: Used to redirect users to a different route
# url_for: Helps build a URL to a specific function dynamically
# render_template: Renders HTML templates
# request: Used to handle incoming HTTP requests (e.g., form data)
# session: Used to store information across requests, like user login state
from flask import Flask, redirect, url_for, render_template, request, session, flash

# timedelta: A class for representing differences in time; commonly used for setting session expiry time.
from datetime import timedelta


# Create an instance of the Flask class, which will be the main app
# The Flask instance will handle all incoming requests and route them accordingly
app = Flask(__name__)

# Secret key is required for session management in Flask
# It is used to securely sign the session cookie to prevent tampering
# You should keep this secret key safe and ideally store it in an environment variable for production use
app.secret_key = "my_secret_key"

# Setting the lifetime of the session to 1 day
# This means the session will remain valid for one day, after which it will expire
app.permanent_session_lifetime = timedelta(days=1)


# Define the route for the home page ('/') and assign it to the 'home' function
# This route is accessed when the user visits http://127.0.0.1:5000/
@app.route("/")
def home():
    # The function returns HTML content, which will be displayed on the homepage
    return render_template("index.html")


# Define a new route for '/test'
# The @app.route decorator binds the function 'test()' to the URL '/test'.
# When a user visits 'http://127.0.0.1:5000/test', this function will be executed.
@app.route("/test")
def test():
    # The 'render_template' function renders an HTML template (in this case, 'test.html').
    # Flask looks for the 'test.html' file inside a folder called 'templates'.
    # Make sure you have a 'templates' folder in the same directory as your Flask app
    # and that 'test.html' is located inside that folder.
    return render_template("test.html")


# Define a dynamic route that accepts a 'name' as a variable in the URL
# The <name> placeholder allows the route to accept different values
# Example: http://127.0.0.1:5000/Stephen will display "Hello Stephen"
@app.route("/<name>")
def greet_user(name):
    # Return a greeting using the 'name' provided in the URL
    return f"Hello {name}"


# Define a route for '/admin' that redirects to the homepage
# If a user tries to access the '/admin' URL, they will be redirected to '/'
@app.route("/admin")
def admin():
    # Use the 'redirect' function to send the user to the 'home' route
    # 'url_for' dynamically generates the URL for the 'home' function
    return redirect(url_for("home"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]  # 'nm' should match the input name in the login form
        session["user"] = user  # Store the username in the session
        flash("Login Successful")
        return redirect(url_for("user"))  # Redirect to user page
    else:
        # Check if 'user' is in the session
        if "user" in session:
            flash("Already Logged In")
            return redirect(url_for("user"))  # Redirect to user page if already logged in
        return render_template("login.html")  # Render login page if not logged in


@app.route("/user")
def user():
    # Check if 'user' is in the session
    if "user" in session:
        # Retrieve the user from the session
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        # If 'user' is not in session, redirect to the login page
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    user = session.get("user")  # Get 'user' from the session, if it exists
    flash(f"You have been logged out, {user}!", "info")  # Use Python f-string for formatting
    session.pop("user", None)  # Removes 'user' from the session
    return redirect(url_for("login"))  # Redirects to the login page


# This block ensures that the Flask app runs only if the script is executed directly
# If this script is imported as a module in another script, this block won't run
if __name__ == "__main__":
    # Run the Flask app with debug mode enabled (helps with error messages and live code reloading)
    app.run(debug=True)
