# coding:utf-8
# author:wuliwen
import yaml


class Opera_file():
	def __init__(self, yaml_path=None):
		if yaml_path:
			self.yaml_path = yaml_path
		else:
			self.yaml_path = r'E:\studypython\day1\dataconf\login.yaml'
		self.yaml = self.redyaml()

	# 从yaml文件读取全部数
	def redyaml(self):
		with open(self.yaml_path, encoding='utf-8') as file1:
			fil = yaml.load(file1.read(), Loader=yaml.SafeLoader)
		return fil

	# 这个是用来读取ddt文件的，这里 我们不用ddt数据驱动
	# def redfile(self,ddt_path):
	# 	data = []
	# 	with open(ddt_path, 'r', encoding='utf-8') as fp:
	# 		for line in fp.readlines():
	# 			data.append(line.strip('\n').split(','))
	# 	return data

	# 从yaml 中读取对应的key 值
	def read_from_yaml(self, key):
		dict = self.redyaml()
		data = dict.get(key)
		return data


# if __name__ == '__main__':
# 	a = Opera_file()
# 	c = a.read_from_yaml('login4')
# 	print(c)
# 	print(type(c))
