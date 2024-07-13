# Flask Celery Email Sending Project

This project demonstrates how to set up a Flask application with Celery to send emails asynchronously using Gmail's SMTP server.

## Prerequisites

- Python 3.x
- Flask
- Celery
- RabbitMQ (as Celery broker)
- Gmail account (for SMTP server)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. install dependencies
3. Configure Gmail SMTP settings:

Replace your-email@gmail.com and your-email-password with your Gmail credentials in send_email() function.
4. Start RabbitMQ server:

Install RabbitMQ if not already installed.
Start RabbitMQ server.
5. Run  ngrok
```bash
ngrok http 80
```
6. Run Celery worker:
```bash
celery -A app.celery worker --loglevel=info
```
7. Run Flask application:
```bash
python app.py
```
8. Usage
Sending Email: ngrok endpoint /?sendmail=<recipient-email> endpoint to queue an email to <recipient-email>.
Logging: ngrok endpoint /?talktome=true endpoint to log the current time in messaging_system.log.
