#coding:utf-8
#author:wuliwen
#SyntaxError: can't assign to function call   意思是不能分配给函数调用
class AA:


	def __init__(self,a,b,n):   #实例化时必须要有a,b,n三个实参数，虽然N没用到  K = AA(3,4)相当于给a,b赋值 ，此时e已经为常量了
		self.a = a
		self.b = b
		self.n = n
		self.e = self.add()
		print(self.e)  #一定被执行
	def add(self):
		f = self.a + self.b
		return f
	def add1(self,h):
		m = self.e + h
		return m
	def add2(self,x,y):      #x,y 与a,b 没有关系
		return x+y
		
K = AA(3,4,6)    #给a,b,n赋值了
print(K.e)##3+4
D = K.add()  #  这里就不能带参数了
print(D)####3+4
t = K.add1(10)
print(t)###10+e,,e=7
f = K.add2(4,5)
print(f)###4+5
print(K.n)##6