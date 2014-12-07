# the %d format character
x = "There are %d types of peoples." % 10
binary = "binary"
do_not = "don't"
# the mutilple format characters
y = "Those who know %s and those who %s" % (binary,do_not)

print x
print y
# the use of %r format character
print "I said :%r." % x
print "I said :%s." % x
print "I also said :%s." % y
print "I also said :'%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r." # why is there no variable here?

print 5 % 6
print joke_evaluation % hilarious
print 6 * 7

w = "This is the left side of ..."
e = "a string with a right side."
# the operator "+" can operate two strings
print w + e