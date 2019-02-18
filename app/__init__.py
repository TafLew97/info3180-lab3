from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '3a9c809a5c93b6'
app.config['MAIL_PASSWORD'] = '4385950d5f3023'

mail = Mail(app)
from app import views