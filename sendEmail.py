import smtplib
import ssl
import getpass

port=465
smtp_server='smtp.gmail.com'
sender_email='ssg.ocdlabs@gmail.com'
receiver_email='cynthia_nguyen25@hotmail.com'
password=getpass.getpass()
message='This message was sent by a robot'
context=ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message)
