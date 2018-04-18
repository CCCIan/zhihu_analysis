import sys
import numpy as np
import matplotlib.pyplot as plt

f = open(r"sex.txt")
lines = f.readlines()
a=0
b=0
for line in lines:
    if line == "男\n":
       a=a+1
    else:
       b=b+1
#print(a)
#print(b)

n=a+b
c=a/n*100
d=b/n*100
labels = 'male','female'
fracs = [c,d]
explode = [0.1,0]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
plt.show()
