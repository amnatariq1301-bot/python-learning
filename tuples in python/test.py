# Tuples are immutable lists, they cannot bechanged once created
tup = (1,2,3,4,5)
print(tup)
print(tup[0]) # Accessing the first element of the tuple
# for changing a tuple it first must be converted to a list and then back to a tuple
temp = list(tup)
# addign new item to the tuple
temp[0] = 10
tup = tuple(temp)

#  tuples can be concatenated
tup2 = (6,7,8,9,10)
tup3 = tup + tup2
print(tup3)