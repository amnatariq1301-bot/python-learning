# required arguments
def average(a, b):
    print("the average is: ", (a+b)/2)

average(2, 3)

# default arguments
def average(a= 9, b =10):
    print("the average is:", (a+b)/2)

average()

def name(fname, mname = "john", lname = "doe"):
    print("the name is: ", fname, mname, lname)

name("jane")

# keyword arguments
def name(fname, mname, lname):
    print("the name is: ", fname, mname, lname)
name(mname = "john", fname = "jane", lname = "doe")