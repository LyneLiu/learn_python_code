# -*- coding:utf-8 -*-

people = 15
cars = 10
trucks = 15
# the number of the cars bigger than people?
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not tale the cars."
else:
	print "We can't decide!"
# the number of the trucks bigger than cars?
if trucks > cars:
	print "There are too many trucks."
elif trucks < cars:
	print "Maybe we should take the trucks."
else:
	print "We still can't decide."
# the number of people bigger than trucks?
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."