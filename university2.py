import sys
import jieba
import jieba.analyse
import numpy as np
import matplotlib.pyplot as plt


if __name__=="__main__":

    word_lst = []
    key_list=[]
    for line in open('university.txt'):#1.txt是需要分词统计的文档

        item = line.strip('\n\r').split('\t') #制表格切分
        # print item
        tags = jieba.analyse.extract_tags(item[0]) #jieba分词
        for t in tags:
            word_lst.append(t)

    word_dict= {}
    with open("universityPie.txt",'w') as wf2: #打开文件

        for item in word_lst:
            if item not in word_dict: #统计数量
                word_dict[item] = 1
            else:
                word_dict[item] += 1

        orderList=list(word_dict.values())
        orderList.sort(reverse=True)
        # print orderList
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key]==orderList[i]:
                    if key=="大学":
                       a = str(word_dict[key])
                       wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                       key_list.append(key)
                       word_dict[key]=0
                    if key=="学院":
                       b = str(word_dict[key])
                       wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                       key_list.append(key)
                       word_dict[key]=0
                    if key=="University":
                       c = str(word_dict[key])
                       wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                       key_list.append(key)
                       word_dict[key]=0


labels = 'U of china','C of china','University'
fracs = [a,b,c]
explode = [0.1,0,0]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
plt.show()
