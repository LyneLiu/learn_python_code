print "Let's practice everything."
# the practice of escape characters
print 'You\'d need konw\'bout escapes with \\ that do \n newline and \t tabs.' 
# the use of """: we can print multiple lines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern\n the needs of  love
nor comprehend passion from intuition
and require an explanation
\n\t\twhere there is none.
"""

print "-------------------"
print poem
print "-------------------"

# print with the formatter %s
five = 10 - 2 + 3 -6
print "This should be five:%f" % five
#define the function secret_formula
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans,jars,crates)
# the varibale is the function
start_point = start_point / 10
print "We can also do this way:"
print "We'd have %d beans, %d jars, %d crates." % secret_formula(start_point)