"I am 6'2\" tall." #escape double-quote inside string
'I am 6\'2" tall'  #escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print "let's try:%r." % tabby_cat
print "another try:%s" % persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","\\","|"]:
		print "%s\r" % i,