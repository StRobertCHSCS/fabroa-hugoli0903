# Receive number from user
number = int(input("Enter your number: "))

# Initialize total
total = 0

#compute the number
for i in range(1,number,2):
    total = total + i 
    
# Output total
print(total)