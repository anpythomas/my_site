from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/portfolio")
# def portfolio():
#     return render_template("portfolio.html")
#
# @app.route("/contact")
# def contact():
#     return render_template("contact-updated.html")

app.route("/")
def home():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=False)

