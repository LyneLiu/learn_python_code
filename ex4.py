# there are 100 cars,30 drivers,90 passengers
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
#the capacity of the driven cars 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are ",cars," cars avaliable."
print "There are only ",drivers," drivers avaliable."
print "There will be ",cars_not_driven," empty cars today."
print "We hava ",passengers," passengers to carpool today."
print "We have the carpool_capacity:",carpool_capacity
print "We need to put about ",average_passengers_per_car," in each car."