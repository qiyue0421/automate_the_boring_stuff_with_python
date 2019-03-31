import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人
my_sender = '1831545391@qq.com'
# SMTP授权码
my_pass = 'dnykhajmasvhffeg'
# 收件人
my_user = '1551124353@qq.com'


def mail():
    ret = True
    try:
        # 邮件内容
        msg = MIMEText('辣鸡邮件', 'plain', 'utf-8')
        # 发件人昵称和邮箱
        msg['From'] = formataddr(['lsp', my_sender])
        # 收件人昵称和邮箱
        msg['To'] = formataddr(['jxw', my_user])
        # 主题
        msg['Subject'] = 'say hello'
        # 构建SMTP对象
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录服务器
        server.login(my_sender, my_pass)
        # 发送邮件
        server.sendmail(my_sender, [my_user,], msg.as_string())
        # 断开服务器
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print('邮件发送成功！')
else:
    print('抱歉，邮件发送失败。')
