# Maligad, Juan Alphonso D.
# 11/14/18
# Activity 2 - Inputs and Conditions
import statistics

x = input().split(',')
studa, grade1 = x[0], statistics.mean([int(i) for i in x[1:]])
y = input().split(',')
studb, grade2 = y[0], statistics.mean([int(l) for l in y[1:]])
if grade1 > grade2:
    print(studa , " got a higher average of " , format(grade1,'.1f'))
else:
    print(studb , " got a higher average of " , format(grade2,'.1f'))

        

        