# Maligad, Juan Alphonso D.
# 12/05/2018
# Activity 04 - Lists, Tuples, Dictionaries

x, y = input().split()
a = []
for i in range(int(x),int(y)+1):
    a.append(i)
b = {"even": [], "odd": []}
for i in a:
    if i %2 == 0:
        b["even"].append(i)
    else:
        b["odd"].append(i)

print(b)