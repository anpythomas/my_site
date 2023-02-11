from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download_resume():
    path = "Andy_Thomas_Resume_G4A copy.pdf"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=False)

