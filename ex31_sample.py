print "It's sunshiny today. Do you want to go out? yes/no"
# the answer
answer = raw_input(">")
# when the answer is yes
if answer == "yes":
	print "You decide to go out, but it is cold. Do you want to dress warm clothes? yes/no"

	dress = raw_input(">")
	if dress == "yes":
		print "Do some practice, and stay healthy!"
	else:
		print "Maybe you would catch a cold!"
# when the answer is no
elif answer == "no":
	print """
	You don't want to go out. So study hard to gain more knowledge to be stronger!
	Close the door.
	Stay away from the outside world!
	"""
# always hesitate...
else:
	print "You are a so stagerer!!!!"