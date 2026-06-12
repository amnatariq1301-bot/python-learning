f = open("main.txt", "r")
i =0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in maths: {m1*2}")
    print(f"Marks of student {i} in English: {m2*2}")
    print(f"Marks of student {i} in SST: {m3*2}")
    print(line)


f = open("main2.txt", "w")
lines = ["line1", "line2", "line3", "line4"]
for line in lines:
    f.write(line + "\n")
f.close()