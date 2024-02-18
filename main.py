import smtplib
from email.mime.text import MIMEText
from email import *

def send_email(
    subject,
    message,
    from_email,
    to_email,
    smtp_server,
    smtp_port,
    smtp_user,
    smtp_password,
):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # Can be omitted
        server.starttls()  # Secure the connection
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
        print("Your Score Has Been Sent To Your Teacher")
        tprint("See You Next Test")

    except Exception as e:
        print(f"Failed to send email: {e}")


# Usage
send_email(
    subject="Hello from Python",
    message="Name = "
    + str(username)
    + "Score = "
    + str(score)
    + "Wrong = "
    + str(wrong)
    + "Correct ="
    + str(correct),
    from_email="example@gmail.com",
    to_email="example@gmail.com",
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    smtp_user="example@gmail.com",
    smtp_password="",
)
