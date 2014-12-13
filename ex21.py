# define the add function
def add(a, b):
    print "Adding: %d + %d" % (a, b)
    return a + b

# definet the substract function


def substract(a, b):
    print "Substracting: %d - %d" % (a, b)
    return a - b

# define multiply function


def multiply(a, b):
    print "Multiplying: %d * %d" % (a, b)
    return a * b

# define the divide function


def divide(a, b):
    print "Dividing: %d / %d" % (a, b)
    return a / b

# tie the value of function to variable
age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit,type it in anyway.
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print "That becomes:", what, "\nCan you do it by hand?"

what_again = substract(add(age, divide(weight, height)), iq)
print "That what_again becomes:", 
print what_again, "\nCan you do it by hand?"

# def add_string(a,b):
# 	return a + b

# a = raw_input("input the string a:")
# b = raw_input("input the string b:")

# print "the result of adding string is:%s" % add_string(a,b)
