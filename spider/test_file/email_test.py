# coding : utf8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr ='378517225@qq.com' #input('From: ')
password ='1want1tw'# input('Password: ')
to_addr ='yezirui@chinasie.com' #input('To: ')
smtp_server ='smtp.qq.com' #input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('测试是否加密成功……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.starttls()

server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()