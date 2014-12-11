from sys import argv

def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that is enough for the party!"
	print "Get a blanket.\n"

script, cheese_count_1, boxes_of_crackers_1 = argv
cheese_count_2 = input()
boxes_of_crackers_2 = input()
# the raw data always is string 
cheese_count_3 = int(raw_input("cheese_count_3:"))
boxes_of_crackers_3 = int(raw_input("boxes_of_crackers_3:"))
# the variable from command line is string, we need convert it into number
cheese_and_crackers(int(cheese_count_1),int(boxes_of_crackers_1))
cheese_and_crackers(cheese_count_2,boxes_of_crackers_2)
cheese_and_crackers(cheese_count_3,boxes_of_crackers_3)


# straight numbers
# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)
# # give variables
# print "OR,we can use variables from the script:"
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese,amount_of_crackers)
# # give math
# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)
# # combine variables and math
# print "And we can combine the two,variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

