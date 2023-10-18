import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the email parameters
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
receiver_email = 'recipient@example.com'
subject = 'Hello from Python!'
message = 'This is a test email sent from Python.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to Gmail's SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")

    # Close the SMTP server
    server.quit()
except Exception as e:
    print(f"An error occurred: {str(e)}")
