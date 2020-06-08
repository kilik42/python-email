import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


username =  'something@gmail.com'
password = 'letsget it started 2020'

def send_mail(text='Email body', subject='hello world',
              from_email='something@gmail.com',to_emails=None, html = None):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')

    if html != None:
        html_part = MIMEText("<h1>this is working</h1>", 'html')
        msg.attach(html_part)


    msg_str = msg.as_string()
    # log in into smtp server
    server = smtplib.SMTP(host= 'smtp.gmail.com', port = 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()





