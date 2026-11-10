import random

'''
1 for stone
-1 for paper
0 for scissor
'''

# Dictionary to map string input to numbers
youstr = input("Enter your choice (stone/paper/scissor): ")
computer = random.choice([-1, 0, 1])
youDict = {"stone": 1, "paper": -1, "scissor": 0}
reverseDict = {1: "stone", -1: "paper", 0: "scissor"}

you = youDict[youstr]
print(f"\nYou chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}\n")


if computer == you:
        print("It's a Draw!")
else:
    
        if computer == -1 and you == 1:    # Paper vs Stone
            print("You Lose!")
        elif computer == -1 and you == 0:  # Paper vs Scissor
            print("You Win!")
        elif computer == 1 and you == -1:  # Stone vs Paper
            print("You Win!")
        elif computer == 1 and you == 0:   # Stone vs Scissor
            print("You Lose!")
        elif computer == 0 and you == -1:  # Scissor vs Paper
            print("You Lose!")
        elif computer == 0 and you == 1:   # Scissor vs Stone
            print("You Win!")
        else:
          print("Invalid choice! Please enter stone, paper, or scissor.")
