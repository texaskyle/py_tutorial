import smtplib

sender = "evansnjoroge3345@gmail.com"
receiver = "lastidiquaz3345@gmail.com"
password = "password"
subject = "job application"
body = "i am applying for the senior software developer at your company"

# header
message = f"""From: Texas kyle {sender}
To: Njoroge Evans {receiver}
subject:{subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("login successful")
    server.send(sender, receiver, message)
    print("Email send has been successful")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in!!!")



