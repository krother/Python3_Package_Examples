
import smtplib
from email.mime.text  import MIMEText

class MailAccount:
    """
    Stores settings for an email account.
    """
    def __init__(self, server,  login,  password,  sender_email, \
                 sender_name, use_tls=False):
        self.server = server
        self.login = login
        self.password = password
        self.mail = sender_email
        self.sender = '"%s" <%s>'%(sender_name, sender_email)
        self.use_tls = use_tls

    def send_email(self, recipient_email, subject, body):
        """Sends an email to a defined address. """
        # prepare message
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = self.mail
        message["To"] = recipient_email
        msg = message.as_string()

        server = smtplib.SMTP(self.server)
        server.set_debuglevel(1)

        if self.use_tls: # deliberately starts tls if using TLS
            server.ehlo()
            server.starttls()
            server.ehlo()

        server.login(self.login, self.password)
        server.sendmail(self.mail, recipient_email, msg)
        server.quit()

if __name__ == '__main__':
    accounts = [
        MailAccount('mailserver_address', \
                'your_account', 'your_password', 'your_email', \
                'Your Name', use_tls=True),
        ]

    for account in accounts:
        try:
            account.send_email('test@testdomain.de', 'Title', 'Content')
            print ('\nSENT!!\n\n\n')
        except smtplib.SMTPAuthenticationError:
            print ('\nFAIL\n\n')
