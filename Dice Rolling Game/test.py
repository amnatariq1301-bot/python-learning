import random

while True:
    choice = input("Do you want to roll the dice? (yes/no): ").lower()
    if choice == "yes":
        dice_roll = random.randint(1,6)
        dice_roll2 = random.randint(1,6)
        print(f"You rolled the dice and got ({dice_roll}, {dice_roll2})!")

    elif choice == "no":
        print("Thanks for playing")

    else:
        print("Invalid choice")
        break
