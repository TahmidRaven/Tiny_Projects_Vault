import smtplib, ssl

port = 456
smtp_server = "smtp.gmail.com"
sender_email = "SENDER@gmail.com"
receiver_email = "RECEIVER@gmail.com"

password = "gmjg skhe xeqo cvpg"

message = """\
    
    Subject: Hello, There. It's Obiwan Kenobi
    
    Wanna be my padawan?"""
    
context = ssl.create_default_context()
context.timeout = 10  # Increase the timeout value to 10 seconds


with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    