"""
This module has maths Functions that compute areas of shapes
"""

 
def square(side):
    """
    This module calculates area of a square.
    """
    area=side*side
    print('The area of square is ',area)
def circle(r):
    """
    
    This module calculates the area of a circle.

    area = side*side
    
    
    """
    import math
    area= math.pi*(r*r)
    print('The area of circle is ',area)
    
def triangle(base,height):
    """
    This module calculates the area of a traingle
    
    area= 1/2(base * height)
    """
    area=0.5*(base*height)
    print('The area of triangle is ',area)
    
def trapezium(base1,base,height):
    """
    This module calculates the area of a trapezium
    
    area= 1/2(a+b)*height
    """
    area=0.5*(base1+base)*height
    print('The area of trapezium is ',area)
    
def  rectangle(length,width):
    """
    This module calculates the area of a rectangle
    
    area = length * width
    """
    area= length*width
    print('The area of rectangle is ',area)
        

