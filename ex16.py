# import the module
from sys import argv
# receive the value from the command line
script,filename = argv

print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that,hit ENTER."

raw_input("?")
# use the open function to open the file
print "Opening the file..."
# when use the mode 'w+',it will truncate the file
target = open(filename,'w+')
# empty the file
# print "Truncating the file. GoodBye!"
# target.truncate()

print "Now I'm going to ask you for three lines."
# receive three lines stuffs
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file."
# write the lines into the file
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1+"\n"+line2+"\n"+line3+"\n")

print "And finally,we close it."
target.close()