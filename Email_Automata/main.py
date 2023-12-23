import smtplib
import ssl

port = 465  # Using port 465 for SMTP_SSL
smtp_server = "smtp.gmail.com"
sender_email = "SENDER@gmail.com"    # add your email
receiver_emails = ["power@gmail.com", "rockz00@gmail.com", "endless@gmail.com", "xbr@gmail.com", "henrybins@gmail.com"] # dummy emails --> provide receivers. Can be a list of emails


password = "gmjg skhe xeqo cvpg"   # my sender gmail's secure app password; biz ecc "endless"

message = """\
Subject: Hello, There.

I'm Jedi Master Obiwan Kenobi. Looking for a new padwan as my previous padwan betrayed our
Jedi Order. Wanna be my padawan? I can feel the force in you. It is quite strong. Surely, Master Yoda
would approve of you. What do you say, youngling? Will you join me in my quest to bring peace to the Galaxy?"""

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context, timeout=10) as server:
        server.login(sender_email, password)
        
        # Iterating over the list of receiver emails and send the message to each one
        for receiver_email in receiver_emails:
            server.sendmail(sender_email, receiver_email, message)
            
        print("Emails sent successfully!")
except smtplib.SMTPException as e:
    print(f"Error: {e}")
