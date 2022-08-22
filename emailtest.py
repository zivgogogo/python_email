import smtplib
from email.mime.text import MIMEText

# 基本信息定义
smtp_server = 'smtp.163.com'  # smtp服务器
port = 25  # SMTP协议默认端口为25

from_address = '自己的邮箱'  # 邮件发件人,改成自己的就行
password = '自己邮箱的授权码'  # 密码或邮箱授权码，这个是你的邮箱密码或者授权码，在
to_address = '邮件收件邮箱'  # 邮件收件人，想发给谁

subject = 'Python 邮件测试'  # 邮件主题
content = '这是使用python smtplib+email自动发送的邮件'  # 邮件正文

# 构建邮件
msg = MIMEText(content, 'plain', 'utf-8')  # 构建一个MIMEText
msg['Subject'] = subject
msg['From'] = from_address
msg['TO'] = to_address

# 发送邮件
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # 启动安全传输模式
    # server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息，如果没有这一语句，将不打印任何信息
    server.login(from_address, password)  # 邮箱账户登录校验
    server.sendmail(from_address, to_address, msg.as_string())  # 邮件发送
    server.quit()  # 断开smtp连接
    print('发送成功')
except Exception:
    print('发送失败')
