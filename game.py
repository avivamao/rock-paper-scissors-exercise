
import random # import random module for computer selection

print("Welcome to the rock-papaer-scissors game!")

# set up variables

gamelist = ["rock", "paper", "scissors"] # define the list
player_selection = input ("Please choose from 'rock', 'paper' or 'scissors':") # ask player to input

# validate player input
player_choice = player_selection.lower()
if player_choice in gamelist:
   print(f"You chose: '{player_choice}'") # if the choice is within the list, print out the choice
else:
    print("Sorry, your choice is not correct.")
    exit() # if the choice is not within the list, print the error message and exit the program

# simulating Computer Selection
com_choice = random.choice(gamelist)
print(f"The computer chose:'{com_choice}'")

# compare player selection vs computer selection
if player_choice == "rock":
    player_num = 0
if player_choice == "paper":
    player_num = 1
if player_choice == "scissors":
    player_num = 2
if com_choice == "rock":
    com_num = 0
if com_choice == "paper":
    com_num = 1
if com_choice == "scissors":
    com_num = 2
# assign an integral to the three selections ("rock", "paper" or "scissors")

if player_num == com_num:
    print("It's a tie!")
elif com_num != 0 and player_num > com_num:
    print ("Congratulations, you won!")
elif com_num == 0 and player_num == 1 :
    print ("Congratulations, you won!")
else:
    print ("Sorry, the computer won..Try next time.")
# compare the values of user/computer selection and print out the message based on the results

print('Thanks for playing. Please play again!')
exit()