# coding:utf-8
# author:wuliwen


# from day1.utils.operaExcel import Opera_Excel
#
#
# class Do_depend:
# 	def __init__(self):
#
# 		self.oper = Opera_Excel()
# 	#根据值来找对应的键，好像用不到，所以这个类没啥用，可以删除
# 	#因为要用到发送请求的模块，所以放到发送请求模块中去了
# 	def get_key_by_value(dict,value):
# 		a = [k for k,v in dict.items() if v == value][0]
# 		return a
#
#
# 	#获取依赖字段的值
# 	#先获取依赖字段(格式为'name':'zhangsan ')
# 	def get_dependField_data(self,i):
# 		field = self.oper.get_field_depend(i)
# 		res = self.send_req.send_main(i)
# 		data = res[field]
# 		return data
# 	#获取本次执行的字段名，并将自己请求数据中字段名和字段值更改
# 	#要求依赖字段名不要写进
# 	#这才是真的请求数据
# 	def set_self_kv(self,i):
# 		self_field = self.oper.get_data_depend(i)
# 		self_data = self.oper.data_from_yama(i)
# 		value = self.get_dependField_data(i)
# 		self_data[self_field] = value
# 		return self_data














