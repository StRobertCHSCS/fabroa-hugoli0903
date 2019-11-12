# Here are the Logical Operators: and, or, not
age = int(input("Enter your age: "))
if not(age < 18):
    print("You are eligable to drink")

else:
    print("You are not eligable to drink")

mother = False
father = True

if mother or father:
    print("You may enter the room.")

else:
    print("You may not enter the room.")