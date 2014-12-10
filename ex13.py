# an "import",add features from the Python feature set
# argv is the "argument variable",holding the arguments 
# passed to Python script
from sys import argv

# "unpack" argv
script, first, second, third = argv
# the raw_input
# raw_input_data = raw_input("please input the raw data:")

print "The script is called:",script
# print "Print the raw_input_data:",raw_input_data
print "The first variable is:",first,type(int(first))
print "The second variable is:",second,type(second)
print "The third variable is:",third,type(third)