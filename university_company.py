import csv
import sys
import jieba
import jieba.analyse


filename = 'university_company.csv'
l=0
with open("university_company.txt",'w') as wf:
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            for zhi in row:
                if row[0] == "浙江大学":
                   #print(row[1])
                   if row[1] != '':
                      l = l+1
                      wf.write(row[1]+'\n')
                      break
                   else:
                      break
    
                


if __name__=="__main__":

    word_lst = []
    key_list=[]
    for line in open('university_company.txt'):#1.txt是需要分词统计的文档

        item = line.strip('\n\r').split('\t') #制表格切分
        # print item
        tags = jieba.analyse.extract_tags(item[0]) #jieba分词
        for t in tags:
            word_lst.append(t)

    word_dict= {}
    with open("u_cBar.txt",'w') as wf2: #打开文件

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
                   if str(key).__len__() >=2:
                      if int(str(word_dict[key])) >= 10:
                         wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                         key_list.append(key)
                         word_dict[key]=0
        wf2.write("带有公司注明的用户总数为："+str(l))
