from flask import Flask, render_template, url_for
app = Flask(__name__,static_folder="static")

@app.route("/")
def home():
    return render_template("appointment.html")

if __name__ == '__main__':
    app.run(debug=True)