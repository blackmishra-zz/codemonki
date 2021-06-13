from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello, World!"
    return render_template("home.html")


@app.route("/about")
def about():
    # return "Hello, World!"
    return render_template("about.html")


@app.route("/orders")
def orders():
    # return "Hello, World!"
    return render_template("orders.html")


@app.route("/products")
def products():
    # return "Hello, World!"
    return render_template("products.html")


@app.route("/login")
def login():
    # return "Hello, World!"
    return render_template("login.html")


@app.route("/signup")
def signup():
    # return "Hello, World!"
    return render_template("signup.html")


# app Starter code
if __name__ == "__main__":
    app.run(debug=True, port=8000)
