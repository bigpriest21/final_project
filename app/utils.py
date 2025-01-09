import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_notification(subscriber_email):
    sender_email = "jacobcollinzy6@gmail.com"
    sender_password = "jmjpyndjkjfgqiac"
    recipient_email = "tizzydave4@gmail.com"

    subject = "New Newsletter Subscriber"
    body = f"You have a new subscriber: {subscriber_email}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
