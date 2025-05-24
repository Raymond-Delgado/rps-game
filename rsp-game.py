# Import the random libary to allow the computer to select an option
import random

print('''
+================================================================================================================================+
| Thank you for playing Rock, Paper, Scissors!                                                                                   |
| Your choices make the game exciting—whether Rock crushes Scissors, Paper outmaneuvers Rock, and Scissors slices through Paper. |
| Enter 1 for Rock, 2 for Paper, 3 for Scissors, or q to Quit —let’s see if you can beat the computer what happens next!         |
+================================================================================================================================+
''')

# Determines a winner The case-match statement will go through all the possible options to determine if the player wins or lose
def winner_selector(player, enemy):
  match (player, enemy):
    case('1','1'):
      print('Both players selected Rock -- it is a stalemate!')
    case('2', '2'):
      print('Both players selected Paper -- it is a stalemate!')
    case('3', '3'):
      print('Both players selected Scissors -- it is a stalemate!')
    case('1','3'):
      print('Rock crushes Scissors -- You win!')
    case('2','1'):
      print('Paper outmaneuvers Rock -- You win!')
    case('3','2'):
      print('Scissors slices through Paper -- You win!')
    case('1','2'):
      print('Paper outmaneuvers Rock -- The computer wins!')
    case('2','3'):
      print('Scissors slices through Paper -- The computer wins!')
    case('3','1'):
      print('Rock crushes Scissors -- The computer wins!')

# This while loop is used to ensure that the program does not end after a single round. The user would have to enter 'q' to quit the game.
# Note: Entering 'q' will break the while loop.
while True:
  user_choice = input('Enter - Rock(1), Paper(2), Scissors(3), or Quit (q): ')
  if user_choice == 'q':
    break
  if user_choice != '1' and user_choice != '2' and user_choice != '3':
    print('Please enter 1, 2, or 3.')
  elif user_choice == '1':
    print('You have selected Rock')
  elif user_choice == '2':
    print('You have selected Paper')
  elif user_choice == '3':
    print('You have selected Scissors')

  computer_choice = str(random.randint(1, 4))
  if computer_choice == '1':
    print('The enemy has chosen Rock')
  elif computer_choice == '2':
    print('The computer has chosen Papper')
  elif computer_choice == '3':
    print('The computer has chosen Scissors')

  winner_selector(user_choice, computer_choice)