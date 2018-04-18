import sys
import jieba
import jieba.analyse



if __name__=="__main__":

    word_lst = []
    key_list=[]
    for line in open('company.txt'):

        item = line.strip('\n\r').split('\t') #制表格切分
        # print item
        tags = jieba.analyse.extract_tags(item[0]) #jieba分词
        for t in tags:
            word_lst.append(t)

    word_dict= {}
    with open("companyPie.txt",'w') as wf2: #打开文件

        for item in word_lst:
            if item not in word_dict: #统计数量
                word_dict[item] = 1
            else:
                word_dict[item] += 1

        orderList=list(word_dict.values())
        orderList.sort(reverse=True)
        # print orderList
        o = 0
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key]==orderList[i]:
                    if str(key).__len__() <=4:
                       if str(key).__len__() >=2:
                          if o <= 13:
                             if str(key)=="腾讯":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="百度":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="阿里巴巴":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="微软":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="谷歌":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="360":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="IBM":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="新浪":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="知乎":
                                k = str(word_dict[key])
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="美团网":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="小米":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="京东":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="网易":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1
                             if str(key)=="华为":
                                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                                key_list.append(key)
                                word_dict[key]=0
                                o = o+1





