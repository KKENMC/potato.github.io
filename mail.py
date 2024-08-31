# coding:utf-8
import smtplib
from email.mime.text import MIMEText
import time
 
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
 
from email.mime.image import MIMEImage
 
def SendMail(sender,receivers,cc_mail,mail_pass,content,file,image,subject):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
 
    #message = MIMEText(content, 'plain', 'utf-8')#正文内容   plain代表纯文本
 
    # 构造一个MIMEMultipart对象代表邮件本身
    message= MIMEMultipart()
    message.attach(MIMEText(content, 'html', 'utf-8'))# 正文内容   plain代表纯文本,html代表支持html文本
 
    message['From'] =sender
    message['To'] = ','.join(receivers) #与真正的收件人的邮箱不是一回事
    message['Cc']=','.join(cc_mail)
 
    # subject = '土豆风控-PotatoRiskControl' % time.ctime()
    message['Subject'] = subject  #邮件标题


    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(sender, mail_pass)
    smtpObj.sendmail(sender, receivers+cc_mail, str(message))  #message.as_string()
    smtpObj.quit()
    print(u"邮件发送成功")

 
