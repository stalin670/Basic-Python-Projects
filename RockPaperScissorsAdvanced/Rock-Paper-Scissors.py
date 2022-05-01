
# I've also uploaded another code for this game but this one is best
# Go through the code 
# play around it.
# Date: 01/05/2022

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user=int(input("What do you want to choose? 0 for Rock, 1 for Scissors or 2 for Rock\n"))

choice=[rock,scissors,paper]

computer=random.randint(0,2)

print(f"You choose :\n {choice[user]}\n")
print(f"Computer choose :\n {choice[computer]}\n")

if (user>2 or user<0):
    print("You've enter the invalid number, Please try again!\n")
elif (user==0 and computer==1) or (user==1 and computer==2) or (user==2 and computer==0):
    print("You wins!\n")
elif user==computer:
    print("Draw!\n")
else :
    print("You lose!\n")
