# Maligad, Juan Alphonso D.
# 11/15/18
# Activity 1 - Palindrome - Revised

words = ["warts n straw", "radar", "Racecar", "python"]
for i in range(0,4):
    print("True" if list(words[i].lower().replace(" ","")) == list(reversed(words[i].lower().replace(" ",""))) else "False")