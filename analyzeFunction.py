# нормальний закон розподілу
import matplotlib.pyplot as plt
import numpy as np
import math

TABLVALUE = 2.26
changes = True
n = 10
np.random.seed()
x = 2+np.random.normal(2, 1.5, n) #генєрування елементи за нормальним законом функції(мат.спод,середнє ариф.відх.,кіл.ел)

print(x)

maxValue = x.max()
minValue = x.min()
averageValue = sum(x)/n
sValue2 = sum((i-averageValue)**2 for i in range(n))/n
sValue = n*sValue2/(n-1)

print(maxValue)
print(minValue)
print(averageValue)
print(sValue)
print((maxValue-averageValue)/sValue)
print((averageValue-minValue)/sValue)

fig, ax = plt.subplots()

ax.plot(x,marker="o",linestyle='')

plt.show()

while changes:
    if(((maxValue-averageValue)/sValue)>TABLVALUE):
        x.max = averageValue
        maxValue = max(x)
        changes = True
        print("change was")
    else:   
        changes=False
    if(((averageValue-minValue)/sValue)>TABLVALUE):
        x.min = averageValue
        minValue = min(x)
        changes = True
        print("change was")
    else:   
        changes=False
    ax.plot(x,marker="o",linestyle='')   
    plt.show()

fig, ax = plt.subplots()

ax.plot(x,marker="o",linestyle='')
plt.show()
