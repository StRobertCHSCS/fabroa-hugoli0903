'''
-------------------------------------------------------------------------------
Name:		practice1.py
Purpose:	converting Farenheit to Celsius

Author:	Li.H

Created:	01/10/2019
------------------------------------------------------------------------------
'''


# The purpose of our program
# get farenheiht from user
farenheit = float(input("Enter the Farenheit: "))
# compute celsius from farenheit
celsius = ((farenheit - 32)*5/9)
# output celsius
print("Converting from Farenheit into Celsius, the temperature is", celsius)
