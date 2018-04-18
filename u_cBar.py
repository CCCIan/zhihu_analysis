import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  

X=['ZJU','Neteasy','STU','ALi','Tecent','Baidu','Huawei']
Y=[106,48,42,35,26,15,10]  
fig = plt.figure()
plt.bar(X,Y,0.4,color="green")
plt.xlabel("Company")
plt.ylabel("Comsumers count")
plt.title("University_Company bar chart")


plt.text(-0.2,106.5,'106')
plt.text(0.88,48.5,'48')
plt.text(1.88,42.5,'42')
plt.text(2.88,35.5,'35')
plt.text(3.88,26.5,'26')
plt.text(4.88,15.5,'15')
plt.text(5.87,10.5,'10')

plt.show()  

