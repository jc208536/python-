import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText

def send_mail_domo(sender,to,subject,context):
	# 连接邮件服务器
	conn = smtplib.SMTP_SSL('smtp.qq.com', 465)
	# 登录
	conn.login('123456@qq.com', '授权码')  # 用户名 和授权码
	# 生成邮件发送对象
	email_obj = MIMEMultipart()
	# 邮件主题
	email_obj['Subject'] = Header(subject, 'utf-8').encode()
	# 内容
	context = MIMEText(context, _charset='utf-8')

	email_obj.attach(context)
	# 发送邮件
	conn.sendmail(sender, to, email_obj.as_string())

# send_mail('@qq.com','@163.com','悠悠我心','青青子衿，悠悠我心，但为君故，沉吟至今')

