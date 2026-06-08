a = input("Enter a number")
print(f"Multiplacation table of {a} is")
try:
    for i in range(0,11):
        print(f"{int(a)} x i = {int(a)*i}")
except Exception as e:
    print(e)
print("some important lines of code")


