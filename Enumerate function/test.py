marks = [2, 4, 98, 76, 0, 17, 92]
for index, mark in enumerate(marks):
    print(mark)
    if index ==2:
        print("You are doing great")


fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)