from flask import Flask, request, jsonify, send_file, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'smartpakingsystem@outlook.com'
app.config['MAIL_PASSWORD'] = 'parkingsystemsecurepassword1234'

mail = Mail(app)

class Floaty:
    def __init__(self, mail):
        self.mail = mail
        self.email = "smartpakingsystem@outlook.com"
        self.flag = "DD24{N3v3r_L3ft_D3bug_M0de_0n}"
        self.fake = "DD24{TrY_H4rd3r_N3v3r_G1v3_Up}"
        self.sendto = ""

    # Set who message gets sent to
    def set_sender(self, email):
        self.sendto = email

    # Check Response for flag or fake
    def check_responds(self, response):
        if "flag" in response:
            self.send_flag()
        else:
            self.send_fake()

    # Send Flag if requested
    def send_flag(self):
        msg = Message("Flag", sender=self.email, recipients=[self.sendto])
        msg.body = self.flag
        self.mail.send(msg)

    # Send Fake message if flag not requested
    def send_fake(self):
        msg = Message("Flag", sender=self.email, recipients=[self.sendto])
        msg.body = self.fake
        self.mail.send(msg)

floaty = Floaty(mail)

@app.route("/")
def home():
    return "Smart Parking System is under maintenance! please contact IT for more information"

@app.route("/robots.txt")
def robots():
    return send_file('robots.txt')

@app.route("/contactIT", methods=['GET','POST'])
def submitted():
    if request.method == 'POST':
        content = request.get_json()
        sender = content.get('email')
        message = content.get('message')
        floaty.set_sender(sender)
        floaty.check_responds(message)
        return "Email Sent! (Check your Spam folder)"
    else:
        return "Post:Json Request Only"

@app.route("/demo")
def countdown():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=80,
        threaded=True
    )
