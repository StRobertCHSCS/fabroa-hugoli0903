parrot_talk = str(input("Is the parrot talking? (y/n) "))

yes = "y"
no = "n"

hour = int(input("What is the current hour? "))

if parrot_talk == yes and hour > 7 and hour < 20:
    print("Everything is fine.")

elif parrot_talk == no:
    print("Everything is fine.")

else:
    print("We're in trouble!")