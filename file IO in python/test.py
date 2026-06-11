


# writing to a file

# f = open("myfile.txt", "a")
# content = f.write("hello world")
# f.close()
with open("myfile.txt", "a") as f:
    f.write("hey i am inside")


#  reading from a file

f = open("myfile.txt", "r")
text = f.read()
print(text)
f.close()