question = [["What is the capital of France?", "Paris"]
            , ["What is the largest mammal?", "Blue Whale"],
            ["What is the smallest country in the world?", "Vatican City"],
            ["What is the tallest mountain in the world?", "Mount Everest"],
            ["What is the longest river in the world?", "Nile River"]]


for q in question:
        print(q[0])
        answer = input("enter your answer:")
        if answer == q[1]:
            print("correct, you have won 1000 dollars")
        else:
            print("wrong answer, you have lost the game")
            break
