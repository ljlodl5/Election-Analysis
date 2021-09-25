# Incorporate the random library
import secrets
from typing import TYPE_CHECKING

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = secrets.choice(options)
print(computer_choice)

# User Selection
user_choice =""
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if(computer_choice == user_choice):
    print("Its a Draw!")
elif(computer_choice =="s") and (user_choice =="p"):
    print("Computer Wins!")
elif(computer_choice =="r") and (user_choice =="s"):
    print("Computer Wins!")
elif(computer_choice =="p") and (computer_choice =="r"):
    print("Computer Wins!")
elif(user_choice =="s") and (computer_choice =="p"):
    print("User Wins!")
elif(user_choice =="r") and (computer_choice =="s"):
    print("User Wins!")
else:
    if(user_choice =="p") and (computer_choice =="r"):
        print("User Wins!")