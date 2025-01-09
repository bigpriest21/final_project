from app import app
from flask import render_template, request, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.utils import send_email_notification


# Helper function to send email
def send_email_notification(subscriber_email):
    sender_email = "jacobcollinzy6@gmail.com"  # Your sender email
    sender_password = "jmjpyndjkjfgqiac"  # Your sender email's password
    recipient_email = "tizzydave4@gmail.com"  # Your admin email

    # Create email content
    subject = "New Newsletter Subscriber"
    body = f"You have a new subscriber: {subscriber_email}"

    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Route to render the home page
@app.route('/')
def home():
    return render_template("index.html")

# Route to handle newsletter form submission
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']  # Get email from the form
    try:
        send_email_notification(email)  # Notify admin
        flash("Thank you for subscribing!", "success")  # Feedback to the user
    except Exception as e:
        print(f"Error sending email: {e}")
        flash("Something went wrong. Please try again later.", "danger")
    return render_template("index.html")
