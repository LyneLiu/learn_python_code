# -*- coding:utf-8 -*-
from sys import argv
# get the variable from the command line
script, input_file = argv
# define the function that print the content of file
def print_all(f):
	print f.read()
# call the function f.seek(0)
def rewind(f):
	f.seek(0)
# define the function that print one line when it was called
def print_a_line(line_count,f):
	print line_count,f.readline()
# open the file
current_file = open(input_file)
# print all the content 
print "First let's print the whole file:\n"
print_all(current_file)
# 设置文件中的当前读取位置，初始化偏移位为0
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
# 输出第一行
current_line = 1
print_a_line(current_line,current_file)
# python支持的变量为mutable类型，所以可以重新赋值
# 输出第二行
current_line += 1
print_a_line(current_line,current_file)
# 输出第三行
current_line += 1
print_a_line(current_line,current_file)