# Combining two branches into one
# So instead of this 
number = int(input("Enter a number: "))

if number < 1:
    print("Not between 1 and 10")
    
elif number > 10:
    print("Not between 1 and 10")
    
else:
    print("Between 1 and 10")

# We can make it into a single branch with and
number = int(input("Enter a number: "))

if number < 1 and number > 10:
    print("Not between 1 and 10")

else:
    print("Between 1 and 10")