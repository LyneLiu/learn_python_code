from sys import argv
# import the module os.path 
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s." % (from_file,to_file)

# we could do these two on one line,how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)
# judge exist of the to_file
print "Does the output file exists? %r" % exists(to_file)
print "Ready,hit ENTER to continue,CTRL-C to abort."
raw_input()
# when open the to_file with the mode 'w'
# if the to_file does not exist,it will
# create a file and name it to_file
out_file = open(to_file,'w')
out_file.write(indata)

print "Alright,All done." 
# don't forget to close the opened files
out_file.close()
in_file.close()

# one line version
# from sys import argv;from os.path import exists; script, from_file, to_file = argv;indata = open(from_file).read();out_file = open(to_file,'w');out_file.write(indata);out_file.close()