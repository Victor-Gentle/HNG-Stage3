from flask import Flask, request, jsonify
from celery import Celery
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import logging
import os

app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

import os

# Ensure log directory exists
log_dir = 'C:/Users/NEW USER/var/log/messaging_system.log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging
log_file = os.path.join(log_dir, 'messaging_system.log')
logging.basicConfig(filename=log_file, level=logging.INFO)


# Configure logging
logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

# Celery task to send email
@celery.task
def send_email(recipient):
    msg = MIMEText('This is a test email from Flask Celery app.')
    msg['Subject'] = 'Test Email'
    msg['From'] = 'mbahkenneth399@gmail.com'
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('mbahkenneth@gmail.com', 'jar@2023')
            server.sendmail('mbahkenneth@gmail.com', [recipient], msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email.delay(sendmail)
        return jsonify({'status': 'Email queued successfully'})

    if talktome:
        log_message = f'TalkToMe endpoint accessed at {datetime.now()}'
        logging.info(log_message)
        return jsonify({'status': 'Logged successfully'})

    return jsonify({'status': 'No action taken'})

if __name__ == '__main__':
    app.run(debug=True)
