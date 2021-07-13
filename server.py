from flask import Flask, render_template, request
import smtplib
import os

OWN_EMAIL = os.environ['EMAIL']
OWN_PASSWORD = os.environ['PASSWORD']

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def receive_data():
    data = request.form
    send_email(data['name'], data["email"], data["message"])
    return render_template("index.html")


def send_email(name, email, message):
    email_message = f"Subject:New Quote\n\nName: {name}\nEmail: {email}\nMessage: {message}"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.starttls()
    server.login(OWN_EMAIL, OWN_PASSWORD)
    server.sendmail(
        OWN_EMAIL,
        "pythontesting414@gmail.com",
        email_message
    )
    server.quit()


if __name__ == "__main__":
    app.run(debug=False)

