# coding:utf-8
# author:wuliwen
class Global_var:
	__id = 0
	__url = 1
	__method = 2
	__header = 3
	__case_depend = 4
	__data_depend = 5
	__field_depend = 6
	__is_run = 7
	__data = 8
	__expect = 9
	__result = 10
	__is_pass = 11

	def getid(self):
		return Global_var.__id

	def geturl(self):
		return Global_var.__url

	def getmethod(self):
		return Global_var.__method

	def getheader(self):
		return Global_var.__header

	def get_casedepend(self):
		return Global_var.__case_depend

	def get_datadepend(self):
		return Global_var.__data_depend

	def get_fielddepend(self):
		return Global_var.__field_depend

	def get_isrun(self):
		return Global_var.__is_run

	def getdata(self):
		return Global_var.__data

	def getexpect(self):
		return Global_var.__expect

	def getresult(self):
		return Global_var.__result

	def get_ispass(self):
		return Global_var.__is_pass



# if __name__ == '__main__':
# 	a = Global_var()
#
# 	k1 = a.get_isrun()
# 	k2 = a.get_ispass()
# 	k3 = a.getresult()
# 	print(k1, k2,  k3)
# 	print(type(k2))
