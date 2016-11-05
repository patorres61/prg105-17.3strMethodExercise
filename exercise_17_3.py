# Phyllis Torres
# 17.3 Write an str Method for a Point Class Assignment
# Due 11/17/2016

print('17.3 Write a str Method for a Point Class Assignment \n')
print('Phyllis Torres\n\n')

print('This program will use a method that returns a string representation of a Point class object. ')


# create a point class
class Point:
    """Represents a point in a 2 dimensional space
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

# initialize the instantiated object with the values of 3 and 4 for x and y
p = Point(3, 4)

print ('\nThe point defined is ' + str(p.x) + ', ' + str(p.y))
print ('\nThe following is the point using the __str__ method to print it.\n')

# print the point using the str method defined in the class
print p


