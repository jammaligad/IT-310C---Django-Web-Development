# Maligad, Juan Alphonso D.
# 11/07/2018
# Activity 1
import random

words = ["warts n straw", "radar", "Racecar", "python"]
txt = random.choice(words)
print("The word is: %s" % (txt))
a = txt.lower()
b = reversed(a)

def palindrome(x):
    y = list(x) == list(b) and "True" or "False"
    print(y)

palindrome(a)