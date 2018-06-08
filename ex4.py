
# variable named "cars" equals 100
cars = 100
# variable named "space_in_a_car" equals 4
space_in_a_car = 4.0
# variable named "drives" equals 30
drivers = 30
# variable named passengers equals 90
passengers = 90
#variable "cars_not_drive" equals the sub of cars-drivers
cars_not_driven = cars - drivers
#variable "cars driven" always equals the number of drivers
cars_driven = drivers
#carpool capacity equals the product of space in cars times the number of drivers
carpool_capacity = cars_driven * space_in_a_car
#average number of passengers in each cars equal the number of passengers divided by the number of drivers
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

print ( "Hey %s there." % drivers)
print("")
print ("Hello %s, what are you doing here? hello %s, not much" % ('Jerry','Newman'))
print("Hello %s, what are you doing here?" % 'Jerry', "Hello %s, not much" % 'Newman')
print("")
print ("Hello %s, my name is %s" % ('john', 'mike'))
