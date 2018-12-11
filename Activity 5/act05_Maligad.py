# Maligad, Juan Alphonso D.
# 12/10/2018
# Activity 5 - Frequency

x = int(input())
c = {}
y = ""

for i in range(int(x)):
    y += input()
    i+=1
for i in y:
    if i in c.keys():
        c[i]+=1
    else:
        c[i]=1
for i in c:
    print(i, " has a frequency of ", c.get(i))
