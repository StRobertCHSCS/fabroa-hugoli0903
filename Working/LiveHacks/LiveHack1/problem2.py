'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Calculating the number of pieces of Popeye Chicken each student
and Mr Fabroa will get.

Author:	Li.H

Created:	02/10/2019
------------------------------------------------------------------------------
'''
# Get the number of chicken pieces and students
chicken_pieces = int(input("Enter the number of chicken pieces: "))
students = int(input("Enter the number of students: "))
# Calculate the number of chicken pieces each student will receive
chicken_pieces_distributed = chicken_pieces//students
# Calculate the leftovers
leftover = chicken_pieces % students
# Output the nmber of chicken pieces each student, and Mr Fabroa will receive
print("Each student will receive", chicken_pieces_distributed, end=" ")
print("and Mr. Fabroa will receive", leftover)
