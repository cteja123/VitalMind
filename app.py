from flask import Flask, render_template, url_for, jsonify, request
app = Flask(__name__,static_folder="static")

@app.route("/")
def home():
    return render_template("home.html")

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