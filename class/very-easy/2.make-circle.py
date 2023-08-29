"""
  Your task is to create a Circle constructor that creates a circle 
  with a radius provided by an argument. The circles constructed must have 
  two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r) which give both 
  respective areas and perimeter (circumference).

  For help with this class, I have provided you with a Rectangle constructor 
  which you can use as a base example.

  Examples
    circy = Circle(11)
    circy.getArea()

    # Should return 380.132711084365

    circy = Circle(4.44)
    circy.getPerimeter()

    # Should return 27.897342763877365
"""
from math import pi
class Circle:
  
  def __init__(self, radius) -> None:
    self.radius = radius
    
  def getArea(self):
    return pi * (self.radius ** 2)
    
  def getPerimeter(self):
    return 2 * pi * self.radius
    

circy = Circle(11)
print(circy.getArea())

# Should return 380.132711084365

circy = Circle(4.44)
print(circy.getPerimeter())

# Should return 27.897342763877365
