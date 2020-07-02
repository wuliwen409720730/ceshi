# coding:utf-8
import requests
from day1.utils.operExcel import Opera_Excel
from day1.dataconf.global_var import Global_var
from day1.utils.mock_servre import mocker
from day1.utils.operayaml import Opera_file



class Send_request:

	def __init__(self):
		self.excel = Opera_Excel()
		self.Globals = Global_var()



	def get_request(self, url, data, header=None):
		if header:
			res = requests.get(url, data, header)
		else:
			res = requests.get(url, data)
		return res

	def post_request(self, url, data,header=None):
		if header:
			res = requests.post(url, data,header)
		else:
			res = requests.post(url, data)
		return res

	def send_main(self, method, url, data):
		if method == 'get':
			res = self.get_request(url, data,header=None)
		else:
			res = self.get_request(url, data,header=None)
		return res

	#
	# 先获取依赖字段,获取依赖字段的值(格式为'name':'zhangsan ')
	#这里没有判断依赖案列是否成功的代码，后期可以补上,这里只考虑只有一个依赖数据，多个的话，要用for循环获取，后期可以补上
	#也未考虑嵌套，比如依赖案例有多个，依赖字段有多个，接口获取的值在嵌套里等情况。
	def get_dependField_data(self, i):
		self_field = self.excel.get_data_depend(i)
		n = self.excel.get_id_by_id(i)
		url = self.excel.get_url(n)
		method = self.excel.get_method(n)
		header = self.excel.get_header(n)
		data = self.excel.data_from_yama(n)
		res = self.send_main(method,url,data)
		data = res[self_field]
		return data

	# 获取本次执行的字段名，并将自己请求数据中字段名和字段值更改
	# 要求依赖字段名不要写进EXCEL中，这样我们直接追加进字典就可以了
	# 这才是真的请求数据
	# def set_self_kv(self, i):
	# 	#自己的字段名
	# 	field = self.excel.get_field_depend(i)
	# 	#自己的请求数据
	# 	self_data = self.excel.data_from_yama(i)
	# 	#依赖CASE返回的值
	# 	value = self.get_dependField_data(i)
	# 	#在自己请求数据中加入需要依赖的数据
	# 	self_data[field] = value
	# 	return self_data

	#注意： 依赖的案列如果不执行，要把它执行
	#这里就是重新构造了需要依赖才能执行的请求数据，对原有数据进行更新了，但是没写入EXCEL
	def rebuild_request_data(self,i):
		#依赖CASE返回的值
		value = self.get_dependField_data(i)
		# 自己的字段名
		field = self.excel.get_field_depend(i)
		# 自己的请求数据
		self_data = self.excel.data_from_yama(i)
		# 在自己请求数据中加入需要依赖的数据
		self_data[field] = value
		return self_data



