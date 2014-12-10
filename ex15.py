# import the module sys
from sys import argv
# use the module sys, pass variables from the command line
script, filename = argv
# open the file
txt = open(filename)

# print the file name
print "Here is you file %r:" % filename
# print the content of the file (string?)
print txt.read()
txt.close()

print "Type the filename again:"
# use the raw_input() to input the filename
file_again = raw_input('> ')
# open and print another file or the same file
txt_again = open(file_again)

print txt_again.read()
# It is important to close the file after you open the file
txt_again.close()