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

our_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
game = [ rock, paper, scissors ]
we_choose = game[our_choice]
print(we_choose)

print("Computer chooses:")
computer_choice = random.randint(0,2)
game2 = [rock, paper, scissors]
computer_choose = game2[computer_choice]
print(computer_choose)

if computer_choose == we_choose:
    print("It's a Draw!")
elif computer_choose == 0 and we_choose == 2:
    print("You Lose!")
elif computer_choose == 1 and we_choose == 0:
    print("You Lose!")
elif computer_choose == 2 and we_choose == 1:
    print("You Lose!")
else:
    print("You Win!")
