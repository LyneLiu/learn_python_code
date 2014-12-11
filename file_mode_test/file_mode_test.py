# -*- coding: utf-8 -*-
# 定义要添加的string列表
test = [ "test1\n","test2\n","test3\n" ]

# open文件test.txt定定义打开模式，如：‘a+’
f = open("test.txt","r+")

# 循环输入string列表
try:
	f.seek(0)
	for l in test:
		f.write(l)
finally:
	f.close()