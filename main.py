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

you_choose_str = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
you_choose = int(you_choose_str)

computer_choose = random.randint(0,2)

if computer_choose == 0:
  if you_choose == 1:
    print(f"Computer choose: {rock}\n {paper}\n You Win!")
  elif you_choose == 2:
    print(f"Computer choose: {rock}\n {scissors}\n You lose!")
  elif you_choose == 0:
    print(f"Computer choose: {rock}\n {rock}\n DRAW, try again!")
  else:
    print(f"Computer choose: {rock}\n DUUUUR\n Invalid option, Dumb!")

if computer_choose == 1:
  if you_choose == 2:
    print(f"Computer choose: {paper}\n {scissors}\n You Win!")
  elif you_choose == 0:
    print(f"Computer choose: {paper}\n {rock}\n You lose!")
  elif you_choose == 1:
    print(f"Computer choose: {paper}\n {paper}\n DRAW, try again!")
  else:
    print(f"Computer choose: {paper}\n DUUUUR\n Invalid option, Dumb!")

if computer_choose == 2:
  if you_choose == 0:
    print(f"Computer choose: {scissors}\n {rock}\n You Win!")
  elif you_choose == 1:
    print(f"Computer choose: {scissors}\n {paper}\n You lose!")
  elif you_choose == 2:
    print(f"Computer choose: {scissors}\n {scissors}\n DRAW, try again!")
  else:
    print(f"Computer choose: {scissors}\n DUUUUR\n Invalid option, Dumb!")
