# coding:utf-8
# author:wuliwen
from ddt import ddt, data, unpack
import unittest
from HTMLTestRunner import HTMLTestRunner
from day1.utils.operayaml import Opera_file


# yama文件编写格式注意：不能用TAB，-和:要空一格
@ddt
class TestMK(unittest.TestCase):

	@data(('a', 'xiaoming'), ('b', 'xiaohong'))  # 注意格式
	@unpack
	def test_1(self, x, y):
		print('%s的值是:%s' % (x, y))

	@data(*Opera_file().redfile())
	@unpack
	def test_2(self, a, b):
		print('{}的值是:{}'.format(a, b))

	@data(*Opera_file().redyaml())
	@unpack
	def test_3(self, a, b):
		print('{}的值是:{}'.format(a, b))

#注意不生成报告的原因，右上角设置
#默认使用unittest框架运行，不会生层报告，因为main条件下代码不执行
if __name__ == '__main__':
	print("***********************")
	casepath = r'E:\studypython\day1'
	discover = unittest.defaultTestLoader.discover(casepath, pattern='test*.py')
	reportpath = "E:\\studypython\\day1\\" + "result.html"
	fp = open(reportpath, 'wb')
	runner = HTMLTestRunner(stream=fp, title='报告名称', description='描述').run(discover)
	fp.close()

