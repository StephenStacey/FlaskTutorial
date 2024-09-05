# Import necessary modules from the Flask framework
# Flask: The main class for creating a web application
# redirect: Used to redirect users to a different route
# url_for: Helps build a URL to a specific function dynamically
from flask import Flask, redirect, url_for

# Create an instance of the Flask class, which will be the main app
app = Flask(__name__)

# Define the route for the home page ('/') and assign it to the 'home' function
# This route is accessed when the user visits http://127.0.0.1:5000/
@app.route("/")
def home():
    # The function returns HTML content, which will be displayed on the homepage
    return "Hello! This is the main page <h1>HELLO</h1>"

# Define a dynamic route that accepts a 'name' as a variable in the URL
# The <name> placeholder allows the route to accept different values
# Example: http://127.0.0.1:5000/Stephen will display "Hello Stephen"
@app.route("/<name>")
def user(name):
    # Return a greeting using the 'name' provided in the URL
    return f"Hello {name}"

# Define a route for '/admin' that redirects to the homepage
# If a user tries to access the '/admin' URL, they will be redirected to '/'
@app.route("/admin")
def admin():
    # Use the 'redirect' function to send the user to the 'home' route
    # 'url_for' dynamically generates the URL for the 'home' function
    return redirect(url_for("home"))

# This block ensures that the Flask app runs only if the script is executed directly
# If this script is imported as a module in another script, this block won't run
if __name__ == "__main__":
    # Run the Flask app with debug mode enabled (helps with error messages and live code reloading)
    app.run(debug=True)
