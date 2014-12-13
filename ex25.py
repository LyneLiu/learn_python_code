# -*- coding: utf-8 -*-
def break_words(stuff):
	"""This function will break up words for us."""
	# String Methods:str.split([sep[,maxsplit]]) -> a list of string
	# 返回一个字符串列表，sep用作定界符，maxsplit表示将list分割n次
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	# build-in function
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after poping it off."""
	# 取列表第一个元素并作为返回值
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after poping it off."""
	# 取列表最后一个元素并作为返回值
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)