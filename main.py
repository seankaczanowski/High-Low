"""
High / Low Number Game
Developed by Sean Kaczanowski
December 2018
No Copyright

Simple Card Game
Player guesses if next card is higher or lower
Features
- Simple Card Graphics
- Streak Counter
- Few Bugs (if any)
"""
import random # Loads Random Module
import time # Loads Sleep Module

# Title Screen
print(" ")
print("  +--------------+ ")
print("  | High/Low 1.0 | ") 
print("  +--------------+ ")
print("  ___          ___ ")
print(" |   | higher |   |")
print(" | 8 |  --->  | ? |")
print(" |___| lower  |___|")
print(" ")
print("Is the next number higher or lower?")
print(" ")
print("Press 'h' for Higher and 'l' for Lower.")
print("Press 'x' to Exit")
print(" ")

number2 = random.randint(1, 9) # Initial Number

# Card Print Format Function
def card_print(number): 
  print(" ___")
  print("|   |")
  print("| " + str(number) + " |")
  print("|___|")
  print(" ")

print("Begin!")
card_print(number2)

i = 1 # Counter for Game Loop
streak = 0 # Streak of Correct Answers Counter
while i == 1: # Game Loop
  
  number1 = number2 # Carry Over Number
  guess = input("Higher/Lower? ")
  number2 = random.randint(1, 9) # New Number
  time.sleep(1)
  
  # Exit Option
  if guess == "x":
    i = 0
    exit()
  
  # High Win
  elif guess == "h" and number2 > number1: 
    card_print(number2)
    streak += 1
  
  # High Lose
  elif guess == "h" and number2 < number1: 
    card_print(number2)
    print("Game Over!")
    print("Streak: " + str(streak) + "\n")
    print("----------------")
    print("----------------\n")
    card_print(number2)
    streak = 0
  
  # Low Lose
  elif guess == "l" and number2 > number1:
    card_print(number2)
    print("Game Over!")
    print("Streak: " + str(streak) + "\n")
    print("----------------")
    print("----------------\n")
    card_print(number2)
    streak = 0
  
  # Low Win
  elif guess == "l" and number2 < number1:
    card_print(number2)
    streak += 1
  
  # High / Low Draw - Treated like a win
  elif guess == "l" or "h" and number2 == number1:
    card_print(number2)
    streak += 1

  # Incorrect Input
  else:
    print("Incorrect Input")

    



