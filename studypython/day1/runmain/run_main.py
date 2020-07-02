# coding:utf-8
# author:wuliwen
#执行时EXCEL打开会报错
from day1.utils.operExcel import Opera_Excel
from day1.dataconf.global_var import Global_var
from day1.utils.send_request import Send_request
from day1.utils.send_email import Send_email
from day1.utils.mock_servre import mocker
from HTMLTestRunner import HTMLTestRunner
import unittest
from day1.utils.operayaml import Opera_file
from day1.utils.logger import Logger


class Runmain():

	def __init__(self):
		self.excel = Opera_Excel()
		self.Globals = Global_var()
		self.sendRequest = Send_request()
		self.sendMail = Send_email()
		self.yama = Opera_file()
		self.logger = Logger(__name__)

	def runmain(self):

		pass_list = []
		fail_list = []
		n = self.excel.get_nrows()
		for i in range(1, n):
			is_run = self.excel.get_is_run(i)

			case_id = self.excel.get_id(i)

			self.logger.get_log().debug('CaseID=' + case_id + '开始执行')

			if is_run == 'yes':
				# case_depend = self.excel.get_case_depend(i)

				expect_result = self.excel.get_expect(i)
				url = self.excel.get_url(i)
				method = self.excel.get_method(i)
				header = self.excel.get_header(i)
				data = self.excel.data_from_yama(i)
				self.logger.get_log().debug('测试数据为： %s'%data)
				# if case_depend == None:
				# 	data = self.excel.data_from_yama(i)
				# 	print(data)
				# else:
				# 	data = self.sendRequest.rebuild_request_data(i)
				# 	self.logger.get_log().debug('CaseID=%s,开始执行依赖接口......' % case_id)
				res = self.sendRequest.send_main(method, url, data)
				real_result = res.status_code
				self.logger.get_log().debug('CaseID=%s,执行结束，返回结果为：%s' % (case_id, real_result))

				if real_result == expect_result:
					pass_list.append(i)
					self.excel.write_result(i, 'pass')
					self.logger.get_log().debug('CaseID=%s,执行结束，测试通过' % case_id)
				else:
					fail_list.append(i)
					self.excel.write_result(i, 'fail')
					self.logger.get_log().debug('CaseID=%s,执行结束，测试失败' % case_id)

			else:
				continue
			i += 1
		self.sendMail.send_main(pass_list, fail_list)
		self.logger.get_log().debug('本次接口测试完成，已发送邮件，请注意查收.......')


aa = Runmain()
aa.runmain()
