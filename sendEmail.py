import smtplib
import ssl
import getpass

def sendActual():
	port=465
	smtp_server='smtp.gmail.com'
	sender_email='ssg.dobby@gmail.com'
	receiver_email='dasayson@hotmail.com'
	password=getpass.getpass()
	message='This message was sent by a robot'
	context=ssl.create_default_context()

	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

class MailClient:
	port=465
	smtp_server='smtp.gmail.com'
	sender_email='ssg.dobby@gmail.com'
	context=ssl.create_default_context()

	def getMessage(self, buyer, buying_for):
		message=''
		with open('template.txt', 'r') as f:
			for line in f:
				message+=line.replace('--name--', buyer).replace('--buying_for--', buying_for)

		return message

	def send(self, email, message):
		port=465
		smtp_server='smtp.gmail.com'
		sender_email='ssg.dobby@gmail.com'
		receiver_email=email
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		with open("appPassword.txt", "r") as source:
			for line in source:
				line = line.strip()
				s.login(sender_email, line)
		s.sendmail(sender_email, receiver_email, message)
		s.quit()

#VPN must be off/paused
if __name__=="__main__":
	sendActual()