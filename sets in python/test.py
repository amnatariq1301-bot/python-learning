# sets are the data types that do not contain repeating items
s = {1, 2, 3, 4}
p = {5, 7, 2, 9}
print(s.union(p))

c = s.update(p)
print(c)

print(s.intersection(p))

d = s.intersection_update(p)
print(d)