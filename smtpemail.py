import smtplib
from getpass import getpass
EMAIL_ADDRESS = "自己的邮箱"
EMAIL_PASSWORD = "自己邮箱的授权码"

smtp = smtplib.SMTP('smtp.163.com',25)
import ssl
context = ssl.create_default_context()
smtp = smtplib.SMTP_SSL("smtp.163.com",465,context=context)
smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

