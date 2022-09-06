from flask import Flask, render_template
import flask_bootstrap
import os

port = int(os.environ.get('PORT', 5000))


app = Flask(__name__)
flask_bootstrap.Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

