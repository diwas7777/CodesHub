import smtplib
import getpass
from email.mime.text import MIMEText

def send_email(senders_address,recipients):
    password = getpass.getpass()
    subject = 'About Me'
    msg = '''
        Hello Everyone!
        This is Rajdeep Kumar. Nice to meet you.
        ThankYou.
    '''
    #server initialisation
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senders_address,password)

    #draft my message body
    msg = MIMEText(msg)
    msg['Subject'] =  subject
    msg['From'] = senders_address
    msg['To'] = ", ".join(recipients)
    #msg.set_param('importance','high value')

    server.sendmail(senders_address,recipients,msg.as_string())

send_email(input('From: '),input('To: ').split())
