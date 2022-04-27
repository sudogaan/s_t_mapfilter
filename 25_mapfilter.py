import math 

def area (r):
	"""Area of a circle with radius 'r'."""
	return math.pi * (r**2)

# what if we need to compute the areas for many different circles.

radii = [2, 5, 7.1, 0.3, 10] # list of the radii of different circles

# method 1: direct method

areas = []
for r in radii:
	a = area(r)
	areas.append(a)
areas

# method 2: use 'map' function
# map function has two arguements, the first is a function and the second is your list, tuple or other iterable object

map(area, radii)

# but the output of the map function is not a list, it is a map object which is an iterator over the results, this is more favorable when working with large data, but if we still want, we can convert it to a list 
list(map(area, radii))

# map function
# data: a1, a2, ..., an
# function: f
# map(f, data):

# list of temperature data from the cities around the world
temps = [("Berlin", 29), ("Cario", 36), ("Buenos Aires", 19), ("Los Angeles", 26(, ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]
# our goal is to convert these celcius degrees to fahreneit

c_to_f = lambda data: (data[0], (9/5)*data[1]+32)
list(map(c_to_f), temps))

# filter function: it is used to select certain pieces of data from a list, tuple, or other collection of data.

# suppose you were analyzing some data and you would like to select all values that are above the average
import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
avg

# use the filter function to select the data above the average
filter(lambda x: x>avg, data) # first arguement is function and second arguement is the data
# the filter function will only return the data for whch the function is true
# the returned value is a filter object, but we can turn it into a list
list(filter(lambda x: x>avg, data))

# remove missing data

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
list(filter(None, countries)) # this filters out all values that are treated as false in boolean setting

# in python, the values that are treated as false are the empty string, 0, an empty list, empty tuple, empty dictionary, false, and none


# reduce function, in python 3, it is not a built-in function it has been demoted to the func tools module. 
# reduce function takes function as the first parameter and data as the second, it firstly applies f to the first two terms of data, next it applies f to the output value and to the third value of data, and it repeats this process for every other value present in that data, once it reaches to the last piece of data, it returns the final value 

# to use reduce function
from functools import reduce

# multiply all numbers in a list

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x,y: x*y
reduce(multiplier, data)

# here is how it would look if you multiply the prime numbers using a for loop instead of a reduce function

product = 1
for x in data:
	product = product * x

product

