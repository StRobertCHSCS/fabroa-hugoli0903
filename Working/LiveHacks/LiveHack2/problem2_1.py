'''
-------------------------------------------------------------------------------
Name:		problem2_1.py
Purpose:	Identifying the type of Triangle

Author:	Li.H

Created:	18/11/2019
------------------------------------------------------------------------------
'''

# receive angles from user
a = int(input("Enter the first angle : "))
b = int(input("Enter the second angle : "))
c = int(input("Enter the third angle: "))

# calculate if the angles make up a triangle
if a + b + c != 180:
    print("Error, the angles do not form a triangle")

# calculate the angles
if a == b and a == c and b == c:
    # output the type of triangle
    print("A triangle with angles" , a ,"," , b , ", and" , c , end= " ")
    print("forms an Equilateral triangle")

# calculate the angles
if a == b or and a + b !=c :
    # output the type of triangle
    print("A triangle with angles" , a ,"," , b , ", and" , c , end= " ")
    print("forms an Isoceles triangle")

# calculate the angles
if a != b and a != c and a != b:
    # output the type of triangle
    print("A triangle with angles" , a ,"," , b , ", and" , c , end= " ")
    print("forms a Scalene triangle")