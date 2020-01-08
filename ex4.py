# Comment about the number of 100 being assigned to a variable CARS
cars = 100
# Comment about the floating point number 4.0 being assigned to a variable
space_in_a_car = 4.0
# Comment about the number of drivers available
drivers = 30
# Comment about the number of people acting as passengers
passengers = 90
# Comment about some calculations being done
# to prepare answers for printout below - see line 20
# this is calculating how many cars will not have a driver
cars_not_driven = cars - drivers
# this is calculating how many cars will have a driver
cars_driven = drivers
# this is calculating a carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# this is average number of people per car driven
average_passengers_per_car = passengers / cars_driven

# These are the printouts
# Answers were prepared in calculations above - see line 9
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
