from flask import Flask, render_template
import flask_bootstrap


app = Flask(__name__)
flask_bootstrap.Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)