l = [1, 2, 4, 6, 8, 1]
print(l)
print(l.append(10))
print(l.sort())
print(l.sort(reverse=True))
print(l.reverse())
print(l.index(2))
print(l.count(1))
l.insert(1,899)
print(l)

m= [10, 20, 30, 40, 50]
# the extend() method adds the specified list elements (or any iterable) to the end of the current list. The length of the list will increase by however many elements were added.
m.extend(l)
print(m)