name = str(input("Enter your name: "))

print("Name:" , name)

if name == "Shonda":
    print("Right this way!")
else:
    print("Sorry, we don't have a reservation under that name.")

# Here's another solution
reservation_name = "Shonda"
name = input("Enter a name: ")

if reservation_name == name:
    print("Right this way!")
else:
    print("Sorry, we don't have a reservation under that name.")