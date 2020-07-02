# coding:utf-8
import xlrd
from day1.dataconf.global_var import Global_var
from xlutils.copy import copy
from day1.utils.operayaml import Opera_file

#EXCEL文件保存后缀为xls
class Opera_Excel:

	def __init__(self, excel_file=None, sheet_id=None):
		if excel_file:
			self.excel_file = excel_file
			self.sheet_id = sheet_id

		else:
			self.excel_file = r'E:\studypython\day1\dataconf\cases.xls'
			self.sheet_id = 0
		#为类创建实例
		self.global_var = Global_var()
		self.openyama = Opera_file()
		#调用自己的方法的到一张默认的表
		self.data = self.get_table()
	#获取表中sheet
	def get_table(self):
		data = xlrd.open_workbook(self.excel_file, self.sheet_id)
		sheet = data.sheet_by_index(self.sheet_id)
		return sheet
	#获取行数
	def get_nrows(self):
		return self.data.nrows

	#获取列数
	def get_cloums(self):
		return self.data.ncols

	# 获取一行的内容
	def get_row_values(self, i):
		nclos = self.data.ncols
		date = self.data.row_values(i, start_colx=0, end_colx=nclos)
		return date

	# 获取某一列的内容(好像没啥用)
	# def get_clovalues(self, i):
	# 	nrows = self.data.nrows
	# 	self.data.col_values(i, start_rowx=0, end_rowx=nrows)

	def get_cls_values(self,i):
		n = self.get_nrows()
		id_list = []
		for num in range(n):
			value = self.get_cell_value(num,i)
			id_list.append(value)
			num += 1
		return id_list


	#获取莫单元格类容
	def get_cell_value(self, row, clo):
		return self.data.cell_value(row, clo)
	#获取某一行的URL的值
	def get_url(self, i):
		clo = self.global_var.geturl()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行的请求数据的值
	def get_data(self, i):
		clo = self.global_var.getdata()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行的请求方法的值
	def get_method(self, i):
		clo = self.global_var.getmethod()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行的请求头的值
	def get_header(self, i):
		clo = self.global_var.getheader()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行是否执行的值
	def get_is_run(self, i):
		clo = self.global_var.get_isrun()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行的期望值
	def get_expect(self, i):
		clo = self.global_var.getexpect()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行的案例ID的值
	def get_id(self, i):
		clo = self.global_var.getid()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行的依赖caseid的值
	def get_case_depend(self, i):
		clo = self.global_var.get_casedepend()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行中在本案例中的字段名
	def get_field_depend(self, i):
		clo = self.global_var.get_fielddepend()
		res = self.get_cell_value(i, clo)
		return res

	# 获取某一行的依赖case返回的字段名
	def get_data_depend(self, i):
		clo = self.global_var.get_datadepend()
		res = self.get_cell_value(i, clo)
		return res

	# 保存不能对sheet使用，此方法用于向某一行写入数据
	def write_result(self, i, txt):
		clo = self.global_var.get_ispass()
		data = xlrd.open_workbook(self.excel_file)
		write_data = copy(data)
		sheet_data = write_data.get_sheet(0)
		sheet_data.write(i, clo, txt)
		write_data.save(self.excel_file)

	#请求数据如登录在EXCEL中写login“,但是真实数据在YAML文件中
	#此方法用于根据哪行中的’login‘字段来读取yaml中的请求数据
	def data_from_yama(self,i):
		key = self.get_data(i)
		data = self.openyama.read_from_yaml(key)
		return data

	#通过行号查出依赖案例对应的行号
	def get_id_by_id(self,i):
		case_id = self.get_case_depend(i)
		id_list = self.get_cls_values(0)
		for num in id_list:
			if num == case_id:
				break
			a = id_list.index(num)
		return a




# if __name__ == '__main__':
# 	a = Opera_Excel()
# 	d = a.get_id_by_id(1)
# 	print(d)
# 	c = a.get_expect(3)
#
# 	print(c)
