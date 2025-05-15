import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



def em(receiver):
  
    message = MIMEMultipart('related')

    msg_content = '''<html><body>
      <p> ALERT Beast, something mischievous happening. Take a close look 🤔 </p>
      <p><img src="cid:picture@example.com" width="300" height="300"></p>
      </body></html>'''
    message.attach(MIMEText((msg_content), 'html'))

    with open('sp2.jfif', 'rb') as image_file:
        image = MIMEImage(image_file.read())
        image.add_header('Content-ID', '<picture@example.com>')
        image.add_header('Content-Disposition', 'inline', filename='sp2.jfif')
        message.attach(image)

    sender = "vigilantsquads@gmail.com"
    password = "novebhfswebflrzt"
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Python Test E-mail'
    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender,[receiver],msg_full)
    server.quit()
