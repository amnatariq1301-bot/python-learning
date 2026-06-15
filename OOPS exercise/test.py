class student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+= val
            print(self.name, "your average score is:", sum/3)


s1 = student("amna", [98, 45, 89])
s1.get_avg()

s2 = student("Ali", [60, 88, 98])
s2.get_avg()