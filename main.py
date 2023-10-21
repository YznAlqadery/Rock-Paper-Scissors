#Importing the random module

import random

print("Welcome to Rock, Paper, Scissors, you're going to play against a computer!")
choices = ["Rock","Paper","Scissors"]

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock,paper,scissors]

user_choice = input("Enter your choice: ")

random_number = random.randint(0,2)
computer_choice = choices[random_number]

def print_images():
    user_number = 0
    if(user_choice.lower() == "rock"):
        user_number = 0
    elif(user_choice.lower() == "paper"):
        user_number = 1
    elif(user_choice.lower() == "scissors"):
        user_number = 2
    else:
        print("Not a valid choice")
    print(images[user_number])
    print(images[random_number])

    

if(user_choice.lower() == "rock" and computer_choice.lower() == "paper"):
    print_images()
    print("You lost!")
elif(user_choice.lower() == "paper" and computer_choice.lower() == "rock"):
    print_images()
    print("You won!")
elif(user_choice.lower() == "scissors" and computer_choice.lower() == "rock"):
    print_images()
    print("You lost!")
elif(user_choice.lower() == "rock" and computer_choice.lower() == "scissors"):
    print_images()
    print("You won!")
elif(user_choice.lower() == "paper" and computer_choice.lower() == "scissors"):
    print_images()
    print("You lost!")
elif(user_choice.lower() == "scissors" and computer_choice.lower() == "paper"):
    print_images()
    print("You won!")
elif(user_choice.lower() == computer_choice.lower()):
    print_images()
    print("Draw!")
    
else:
    print("Enter a valid choice!")
    
