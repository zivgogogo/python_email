import smtplib
from getpass import getpass
EMAIL_ADDRESS = "wangjiaheng666@163.com"
EMAIL_PASSWORD = "RROEVRPMKOFPTZGN"

smtp = smtplib.SMTP('smtp.163.com',25)
import ssl
context = ssl.create_default_context()
smtp = smtplib.SMTP_SSL("smtp.163.com",465,context=context)
smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

