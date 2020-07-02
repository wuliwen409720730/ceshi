#coding:utf-8
#author:wuliwen
import sys
import os.path
#获取当前路径
def getcwd():
	return sys.argv[0]
print(getcwd())
def get_atime():
	return os.path.getatime()
def get_ctime():
	return os.path.getatime()
def get_mtime():
	return os.path.getmtime()

