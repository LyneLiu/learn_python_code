my_name = 'Lyne Liu'
my_age = 25 # yeah,it's true
my_height = 180 # centimeters
my_weight = 78 # kilograms
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s."%my_name
print "He's height is %d."% my_height
print "He's %d kg heavy."%my_weight
print "Actually that is not too heavy,^_^."
print "He's got %s eyes and %s hair."%(my_eyes,my_hair)
print "His teeth are actually %s depending on the coffee."%my_teeth

# the total info of is below:
print "my_name:%s,my_age:%d,my_height:%d,my_weight:%d,my_eyes:%s,my_teeth:%s,my_hair:%s"%(my_name,my_age,
	my_height,my_weight,my_eyes,my_teeth,my_hair)
print "If I add %d,%d,and %d,then I get %d."%(my_age,my_height,my_weight,my_age + my_height + my_weight)

#convert the centimeters to inches
print "my_height is %r centimeters,converted to inches is %r inches."%(my_height,my_height*0.3937008)
print "my_weight is %r kilograms,converted to pound is %r pounds."%(my_weight,my_weight/0.45359237)