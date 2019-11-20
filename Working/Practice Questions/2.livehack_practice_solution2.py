'''
-------------------------------------------------------------------------------
Name:		2.livehack_practice_solution2.py
Purpose:	Determining if the triangle is a right angled

Author:	Li.H

Created:	14/11/2019
------------------------------------------------------------------------------
'''
# Receive the side lengths from the user
side_1 = (int(input("Enter the length of Side 1: ")))
side_2 = (int(input("Enter the length of Side 2: ")))
side_3 = (int(input("Enter the length of Side 3: ")))

# Calculate the formula
side_1 = side_1**2
side_2 = side_2**2
side_3 = side_3**2

# Calculate the possibilities
if side_1 + side_2 == side_3:
    print("This is a right angled triangle")
elif side_1 + side_3 == side_2:
    print("This is a right angled triangle")
elif side_2 + side_3 == side_1:
    print("This is a right angled triangle")
else:
    print("This is not a right angled triangle")