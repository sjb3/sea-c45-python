"""circle class --

fill this in so it will pass all the tests.
"""
import math
import pytest

class Circle(object):
    
    def __init__(self, radius):
    	
    	self.radius = radius
    	self.diameter = 2 * radius
    	self.area = math.pi * radius ** 2


    def _get_d(self):
    	return self._diameter

    def _set_d(self, value):
    	self._diameter = value
    	self.radius = value / 2
    	self.area = math.pi * self.radius ** 2

    def _del_d(self):
    	del self._diameter

    diamter = property(_get_d, _set_d, _del_d)
    doc = 'Largest distance between any two points on circle.'

 #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

    def _get_d(self):
        return self._area

    area = property(_get_a)

    doc = "Area of a Circle"

    def __str__ (self):
        return "Circle with radius: {:.6f}" .format(self. radius)

    def __repr__ (self):
        return "Circle ({r})" .format(r=self. radius)

    def __add__ (self. other):
        return Circle(self.radius + other.radius)

    def __mul__ (self. other):
        return Circle(self.radius * other)

    def __eq__ (self. other):
        return self.radius == other.radius

    def __le__ (self. other):
        return self.radius <= other.radius

    def __gt__ (self. other):
        return self. radius >= other.radius

    def __lt__ (self.other):
        return self. radius < other.radius

