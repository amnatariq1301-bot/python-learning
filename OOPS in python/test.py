class student():
    colleg_name = "ABC college"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student to database")

    def hello(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks
    



s1 = student("amna", 97)

print(student.colleg_name)
s1.hello()
print(s1.get_marks())

s2 = student("usman", 98)
print(student.colleg_name)
s2.hello()
print(s2.get_marks())

