import smtplib
import ssl

GMAIL_SMTP = "smtp.gmail.com"
MY_GMAIL = ""
GMAIL_PSSWD = ""

YAHOO_SMTP = "smtp.mail.yahoo.com"
MY_YAHOO = ""
YAHOO_PSSWD = "" # One-Time Password For App - Yahoo Settings

PORT_SSL = "465" # MOSTLY COMMON USED PORT NUMBER
PORT_TLS = "587"

CONTEXT = ssl.create_default_context()

with smtplib.SMTP_SSL(GMAIL_SMTP, PORT_SSL, context=CONTEXT) as server:
    server.login(MY_GMAIL, GMAIL_PSSWD)
    server.sendmail(from_addr="",
                    to_addrs="",
                    msg="Subject: Test Email\n"
                        "Hello This is a test email!",
                    )

# THIS IS TO TEST BACK AND FORTH BETWEEN TWO DIFFERENt SMTP SERVERS 

with smtplib.SMTP_SSL(YAHOO_SMTP, PORT_SSL, context=CONTEXT) as yahoo_server:
    yahoo_server.login(MY_YAHOO, YAHOO_PSSWD)
    yahoo_server.sendmail(from_addr="",
                          to_addrs="",
                          msg="Subject: Test Email\n"
                              "Hello This is a test email.",
                          )




