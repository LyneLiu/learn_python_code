from sys import argv
# variable from the command line
script, user_name = argv
# the propting message
prompt = '>>\n'
# print the message
print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few question."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where it is.
And you have a %r computer. Nice.
""" % (likes,lives,computer)