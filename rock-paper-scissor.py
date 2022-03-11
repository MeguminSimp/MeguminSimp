import random

def space(number):
    for x in range(number):
        print(" ")

choiceList = ["rock", "paper", "scissor"]
game = True

while game:
    userChoice = input("Please Choose (Rock/Paper/Scissor) ")
    space(1)
    computerChoice = random.choice(choiceList)

    userChoice.lower()
    computerChoice.lower()

    print(f"Computer: {computerChoice}")
    space(1)

    if computerChoice == userChoice:
        print("| Draw |")
        space(2)
        
    elif (computerChoice == "rock" and userChoice == "paper") or (computerChoice == "paper" and userChoice == "scissor") or (computerChoice == "scissor" and userChoice == "rock"):
        print("| User Win |")
        space(2)

    elif (computerChoice == "paper" and userChoice == "rock") or (computerChoice == "scissor" and userChoice == "paper") or (computerChoice == "rock" and userChoice == "scissor"):
        print("| Computer Win |")
        space(2)
    else:
        print("| Something went wrong, choose again please. |")
        space(2)
        
