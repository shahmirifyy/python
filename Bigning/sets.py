# 1. add(elem)

s = {1, 2, 3}
s.add(4)
print("add:", s)            # {1, 2, 3, 4}

# 2. clear()
s.clear()
print("clear:", s)          # set()

# 3. copy()
s1 = {1, 2, 3}
s2 = s1.copy()
s2.add(99)
print("copy:", s1, s2)      #s1= {1,2,3}, s2={1,2,3,99}

# 4. difference(*others)
a = {1, 2, 3, 4}
b = {3, 4, 5}
print("difference:", a.difference(b))  # {1, 2}

# 5. difference_update(*others)
c = {1, 2, 3, 4}
c.difference_update({2,3})
print("difference_update:", c)         # {1, 4}

# 6. discard(elem)
d = {1, 2, 3}
d.discard(2)
d.discard(7)            # no error if not present
print("discard:", d)    # {1, 3}

# 7. intersection(*others)
e = {1, 2, 3}
f = {2, 3, 4}
print("intersection:", e.intersection(f))  # {2,3}

# 8. intersection_update(*others)
g = {1, 2, 3}
g.intersection_update({2,3,9})
print("intersection_update:", g)           # {2,3}

# 9. isdisjoint(other)
h = {1, 2}
i = {3, 4}
print("isdisjoint:", h.isdisjoint(i))      # True

# 10. issubset(other)
j = {1, 2}
k = {1, 2, 3}
print("issubset:", j.issubset(k))          # True

# 11. issuperset(other)
l = {1, 2, 3}
m = {1, 2}
print("issuperset:", l.issuperset(m))      # True

# 12. pop()
n = {1, 2, 3}
popped = n.pop()       # arbitrary element
print("pop:", popped, n)

# 13. remove(elem)
o = {1, 2, 3}
o.remove(2)
print("remove:", o)    # {1,3}
# o.remove(5)         # would raise KeyError

# 14. symmetric_difference(other)
q = {1, 2, 3}
r = {3, 4, 5}
print("symmetric_difference:", q.symmetric_difference(r))  # {1,2,4,5}

# 15. symmetric_difference_update(other)
s = {1, 2, 3}
s.symmetric_difference_update({2,3,4})
print("symmetric_difference_update:", s)                   # {1,4}

# 16. union(*others)
t = {1, 2}
u = {2, 3}
print("union:", t.union(u))        # {1,2,3}

# 17. update(*others)
v = {1, 2}
v.update({3, 4}, [5, 6])
print("update:", v)                # {1,2,3,4,5,6}
