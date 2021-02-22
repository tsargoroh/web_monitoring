import smtplib
from email.message import EmailMessage

def send_email(Email_Address, Email_Password, Receiver, failed_web_list):
    content = ""
    for failed_web_page in failed_web_list:
        content = content + f"{failed_web_page[0]} | status: {failed_web_page[1]}" \
                            + f" - {failed_web_page[2]} | response time: {failed_web_page[3]} sec" + "\n"

    msg = EmailMessage()
    msg["Subject"] = "web malfunction"
    msg["From"] = Email_Address
    msg["To"] = Receiver
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(Email_Address, Email_Password)
        smtp.send_message(msg)