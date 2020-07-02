#coding:utf-8
#author:wuliwen
import json
# a = '中国'
# print(dir(a))
# print(a.encode('utf-8').decode('utf-8'))#encode编码，decode解码
# print(a.encode('gbk').decode('gbk'))
# print(a.encode('gbk').decode('utf-8'))#这个可不行哦~不可以这样用


b = {'4': '5', '6': '7'}#字典
# b = {"4": '5', "6": '7'}#字典
 print(type(b))
# c = json.dumps(b)#把字典转为字符窜

# print(type(c))
# print(c)###{"4": "5", "6": "7"}#字符窜
# d =json.loads(c)#把字符窜转为字典
# print(type(d))
# print(d)###{'4': '5', '6': '7'}#字典


# m = (1,2)
# print(type(m))##元祖
# # g = json.loads(m)####json.loads()必须为字符窜才可以
# e = json.dumps(m)
# print(e)
# print(type(e))#字符窜
# f = json.loads(e)
# print(type(f))
# ##总结：dumps方法是转化为字符串，loads方法是将字符窜转化为JSON对象
# p = 'sdfsa'
# print(p)###控制台输出sdfsa,而不是"sdfsa"