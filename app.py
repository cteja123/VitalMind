from flask import Flask, render_template, url_for, jsonify, request
from flask_mysqldb import MySQL

# import mysql.connector
app = Flask(__name__,static_folder="static")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "test"

mysql = MySQL(app)

@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("select * from countries")
    fetch_data = cur.fetchall()
    cur.close()
    return render_template("home.html",data = fetch_data)

@app.route("/appointment")
def appointment():
    return render_template("appointment.html")

@app.route("/bookanappointment", methods=["GET", "POST"])
def bookanappointment():
    if request.form:
        return jsonify({"status": "success", "message": "Appointment booked successfully!","output":request.form}),200
    else:
        return jsonify({"status": "error", "message": "No form data received"}), 400

if __name__ == '__main__':
    app.run(debug=True)