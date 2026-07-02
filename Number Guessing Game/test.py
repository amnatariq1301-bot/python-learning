import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        user_input = int(input("Guess the Number between 1 and 100: "))
        if user_input < number_to_guess:
            print("Too low! Try again.")    
        elif user_input > number_to_guess:
            print("Too high! Try again.")   
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid integer.")
