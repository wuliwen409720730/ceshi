#coding:utf-8
#author:wuliwen
from day1.runmain import run_main
import unittest
from HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):

	def test01(self):
		self.runmain = run_main.Runmain.runmain()

if __name__ == '__main__':
	casepath = r'E:\studypython\day1\runmain'
	discover = unittest.defaultTestLoader.discover(casepath, pattern='test*.py')
	reportpath = "E:\\studypython\\day1\\report\\result1.html"
	fp = open(reportpath, 'wb')
	runner = HTMLTestRunner(stream=fp, title='报告名称', description='描述').run(discover)
	fp.close()
