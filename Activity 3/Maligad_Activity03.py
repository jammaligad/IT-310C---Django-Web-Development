# Maligad, Juan Alphonso D.
# 11/28/18
# Activity 3 - Python script that will accept two string inputs separated by a whitespace containing alphanumeric characters. Create a function that would extract all alpha (a-z, A-Z) characters from the two inputs and store it as a single string. The function should also extract all numbers from both inputs and add them.

def extract(inx, iny):
    a = ""
    b = 0
    for i in inx:
        if i.isalpha() == True:
            if i not in a:
                a += i
        else:
            b += int(i)
    for l in iny:
        if l.isalpha() == True:
            if l not in a:
                a += l
        else:
            b += int(l)
    print(a.lower(), b)

an1, an2 = input().split(" ")
extract(an1, an2)
