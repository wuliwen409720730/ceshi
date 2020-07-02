#coding:utf-8
#author:wuliwen
#不太会用，后期学习
from unittest import mock
import unittest



#为什么mock_method是灰色的
def mocker(mock_method,request_data,url,method,respons_data):
	mock_method = mock.Mock(return_value=respons_data)
	res = mock_method(url,method,request_data)

	return res