import smtplib

from asdf import outputText
# sender='vishuboy.dreams@gmail.com'
# receiver='vishal.14bcs2018@abes.ac.in'
# password=""
# smtpserver=smtplib.SMTP("smtp.gmail.com",587)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo
# smtpserver.login(sender,password)
# msg=outputText
# smtpserver.sendmail(sender,receiver,msg)
# print('Sent')
# smtpserver.close()

# Import smtplib to provide email functions

# Import the email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define email addresses to use
addr_to = 'vishal.14bcs2018@abes.ac.in'
addr_from = "vishal.14bcs2018@abes.ac.in"

# Define SMTP email server details
smtp_server = 'smtp.gmail.com'
smtp_user = 'vishuboy.dreams@gmail.com'
smtp_pass = 'xxxxxx'

# Construct email
msg = MIMEMultipart('alternative')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Test Email '

# Record the MIME types of both parts - text/plain and text/html.

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(MIMEText(outputText, 'html'))

# Send the message via an SMTP server
s = smtplib.SMTP(smtp_server, 587)
s.ehlo()
s.starttls()
s.login(smtp_user, smtp_pass)
s.sendmail(addr_from, addr_to, msg.as_string())
s.quit()
