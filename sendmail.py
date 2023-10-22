from userInfo import *
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def sendMail():
    receiver_email = str(input("who is the receiver?\t"))

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "PDF file"


    # PDF dosyasını eklemek
    pdf_filename = "table.pdf"
    attachment = open(pdf_filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % pdf_filename)
    msg.attach(part)

    # E-posta sunucusuna bağlanma ve e-postayı gönderme
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print("E-posta gönderme hatası:", str(e))
