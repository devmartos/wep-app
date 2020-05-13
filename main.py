from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")\

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")\

@app.route("/templates/boogle")
def boogle():
    return render_template("login.html")\

@app.route("/templates/FakeBook")
def fakebook():
    return render_template("FakeBook.html")\


@app.route("/templates/peluqueria")
def peluqueria():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()