# coding:utf-8

# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 用于构建邮件头
from email.header import Header


class Send_email:
	global send_user
	global password
	global email_host
	send_user = "409720730@qq.com"
	# 发信服务器
	email_host = 'smtp.qq.com'
	password = 'vbidvjceqjnpbhgc'  # 这里是授权码，不是邮箱密码,去自己手动开启获得

	def build_email(self, user_list, sub, content):
		user = "往后余生" + "<" + send_user + ">"
		# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
		message = MIMEText(content, 'plain', 'utf-8')
		message['subject'] = sub
		message['from'] = user
		message['to'] = ';'.join(user_list)
		# 开启发信服务
		server = smtplib.SMTP()
		# 连接服务器
		server.connect(email_host)
		# 登录服务器
		server.login(send_user, password)
		# 发送邮件
		server.sendmail(user, user_list, message.as_string())
		# 关闭
		server.close()

	def send_main(self, pass_list, fail_list):
		pass_num = float(len(pass_list))
		fail_num = float(len(fail_list))
		total_num = float(pass_num + fail_num)
		pass_percentage = '%.2f%%' % (pass_num / total_num * 100)
		fail_percentage = '%.2f%%' % (fail_num / total_num * 100)
		content = '本次接口测试共测试接口个数为:%s个，成功个数为%s个，失败个数为%s个，成功率为%s个，失败率为%s' % (total_num, pass_num, fail_num, pass_percentage, fail_percentage)
		#收件人列表，可添加多个
		user_list = ['409720730@qq.com',]
		sub = '这是本次接口测试结果'
		self.build_email(user_list,sub,content)



# if __name__ == '__main__':
# 	sen = Send_email()
#
# 	sen.send_main([1,2,3,4],[2,3,4,5,6])

# 发信方的信息：发信邮箱，QQ 邮箱授权码
# from_addr = 'xxx@qq.com'
# password = '你的密码'
#
# # 收信方邮箱
# to_addr = 'xxx@qq.com'
#
# # 发信服务器
# smtp_server = 'smtp.qq.com'
#
# # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
# msg = MIMEText('send by python', 'plain', 'utf-8')
#
# # 邮件头信息
# msg['From'] = Header(from_addr)
# msg['To'] = Header(to_addr)
# msg['Subject'] = Header('python test')
#
# # 开启发信服务，这里使用的是加密传输
# server = smtplib.SMTP_SSL()
# server.connect(smtp_server, 465)
# # 登录发信邮箱
# server.login(from_addr, password)
# # 发送邮件
# server.sendmail(from_addr, to_addr, msg.as_string())
# # 关闭服务器
# server.quit()
