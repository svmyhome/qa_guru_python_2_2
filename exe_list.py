#TODO List
#TODO multiplicity
#TODO dictionary

import copy
l = [1,2,3,["key", "value", "name","Ivan"],5]
print(l)
l1 = l
print(f"L1 is only link to l {l1}")
l2 = l.copy()
print(f"L2 is apartly link to l {l2}")
l3 = copy.deepcopy(l)
print(f"L3 is unlink to l {l2}")

print(l[0:3])
print(l[::-1])
print(l[3])
print(l.pop(1))
print(l)
print(l)
print(l)

s = {1,2,3,4,5}
print(s)


d = {
    "key": "value",
    "name": "Ivan"
}

print(d["key"])
print(d["name"])
print(d.items())