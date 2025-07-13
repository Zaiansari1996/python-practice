#Making A Dice Roll Simulator
import random
while True:
    print(input("Press Enter to Roll The Dice"))
    print("Your Rolled The Dice:", random.randint(1,6))
    again = input("Roll Again?\nPress 'y' for  Yes\nPress 'n' for No\n ")
    if again != 'y':
        break
print("Simulator Ended")
