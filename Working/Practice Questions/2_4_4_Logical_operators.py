# Receive the numbers from user
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number:"))

# Compute the numebrs
if first_number == 10 or second_number == 10:
    print("True")

elif first_number + second_number == 10:
    print("True")

else:
    print("False")