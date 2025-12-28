import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./mail_message.html').read_text())
email = EmailMessage()
email['from'] = 'André'
email['to'] = 'user@email.com'
email['subject'] = 'Hello from python'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@email.com', 'jmwl wplv wxmb zmtx')
    smtp.send_message(email)
    print('all good boss!')
