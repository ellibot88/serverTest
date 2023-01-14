import smtplib, ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication
 
# creates SMTP session
s = smtplib.SMTP_SSL('smtp.ionos.com', 465)
 
# start TLS for security

 
# Authentication
s.login("elliott@hack-a-thon.com", "Lltbob166390")
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail("elliott@hack-a-thon.com", "bdd1da709e9147fe82e526a523547f28@hack-a-thon.mail.domo.com", message)
 
# terminating the session
s.quit()




