import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  

X=['ZJU','WHU','PKU','HUST','SYSU','THU','SJTU','FDU','NJU','SCU']
Y=[3858,3563,3381,3265,3166,3002,2693,2521,2415,2249]  
fig = plt.figure()
plt.bar(X,Y,0.4,color="green")
plt.xlabel("University")
plt.ylabel("Comsumers count")
plt.title("University bar chart")


plt.text(-0.35,3858,'3858')
plt.text(0.65,3563,'3563')
plt.text(1.65,3381,'3381')
plt.text(2.65,3265,'3265')
plt.text(3.65,3166,'3166')
plt.text(4.65,3002,'3002')
plt.text(5.65,2693,'2693')
plt.text(6.65,2521,'2521')
plt.text(7.65,2415,'2415')
plt.text(8.65,2249,'2249')

plt.show()  
plt.savefig("universityBar.jpg")
