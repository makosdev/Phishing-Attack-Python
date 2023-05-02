import smtplib

# Define the email addresses
sender_email = "attacker@gmail.com"
receiver_email = "victim@gmail.com"

# Define the message content
message = """
Subject: Important Account Update

Dear Valued Customer,

We have detected some unusual activity on your account. To ensure your security, we need you to verify your account information by clicking on the following link: 
http://fake-website.com/account-verification/

Thank you for your cooperation.

Best regards,
Your Bank
"""

# Define the email server and login credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "attacker@gmail.com"
password = "password"

# Create a secure SMTP connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    # Send the email
    server.sendmail(sender_email, receiver_email, message)
