import smtplib
import config 
'--------------------'
subject= 'test'
msg='salut'
'--------------------'
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        
        server.login(config.EMAIL_ADRESS, config.PASSWORD)
        message = 'Subject : {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADRESS, config.DESTINATAIRE, message)
        server.quit
        print('Email envoyer')
    except:
        print('salut')
       


'--------------------'

send_email(subject, msg)