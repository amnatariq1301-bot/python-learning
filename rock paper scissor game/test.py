import random
choice = input("Enter your choice (rock, paper, scissors): ").lower()
while True:
    try:
        if choice == "rock":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print("You chose rock.")
            print(f"computer chose {computer_choice}")
            if computer_choice == "rock":
                print("its a tie")
            elif  computer_choice == "paper":
                print("computer wins")
            else:
                print("you win")
        elif choice == "paper":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print("You chose Paper.")
            print(f"computer chose {computer_choice}")
            if computer_choice == "rock":
                print("You won")
            elif  computer_choice == "paper":
                print("Its a tie")
            else:
                print("Computer wins")

        else:
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print("You chose Scissors.")
            print(f"computer chose {computer_choice}")
            if computer_choice == "rock":
                print("computer won")
            elif  computer_choice == "paper":
                print("You won")
            else:
                print("its a tie")
        break
    except ValueError:
        print("Invalid input. Please enter rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()