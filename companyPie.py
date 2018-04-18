import sys
import numpy as np
import matplotlib.pyplot as plt


labels = 'BAT','MulTech','Other'
fracs = [1395+1087+877,344+232+222,579+515+251+226+212+205+203+199]
explode = [0.05,0.1,0.05]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
plt.show()
