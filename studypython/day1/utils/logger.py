#coding:utf-8
#author:wuliwen
import logging
import os
from day1.utils.getcwd import getcwd
log_path = getcwd()
# print(log_path)

class Logger:
	#实例化时填入loggername
	#t通过getLogger（loggername）创建一个log对象，然后设置等级
	def __init__(self,loggername):
		#创建一个logger
		self.loggername = loggername
		self.logger = logging.getLogger(loggername)
		self.logger.setLevel(logging.DEBUG)
		self.log_path = getcwd()
		#创建一个handler,用于写入日志文件
		log_path = os.path.dirname(getcwd()) + '/logs/'
		# log_name = log_path + 'out.log'
		fh = logging.FileHandler(self.loggername.encode('utf-8'))
		fh.setLevel(logging.DEBUG)

		#创建一个handler,用于将日志输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)

		#定义handler的而输出格式
		formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		#给logger添加handler
		self.logger.addHandler(fh)
		self.logger.addHandler(ch)

	def get_log(self):
		return self.logger

if __name__ == '__main__':
	t = Logger('wuliwen').get_log().debug('User %s is logging' %'wuliwen')
	print(log_path)