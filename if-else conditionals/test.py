import time
time = int(time.strftime("%H", time.localtime()))
name = input("Enter your Name: ")
if 4 > time < 12:
    print("good Morning", name)
elif 12 >= time <= 17:
    print("good Evening", name)
else:
    print("good Night", name) 