from sys import argv
# receive the value from the command
script, filename = argv

print "I'm access the file %r." % filename
# open the file
txt = open(filename)

# read the content of the file what I wrote in the running of ex16.py
# and print it
raw_input("the content of the file is:")
print txt.read()

#close the file
txt.close()