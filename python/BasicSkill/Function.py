
################################################################################################################################
#函数
################################################################################################################################
# #带默认参数
# def fun(a=1,b=2):
#     return a+b
# print(fun())  

#如果函数参数有些是默认参数，有些是没有默认的，没有默认参数要写在前面，否则编译要报错
#如 def fun(a=1,b=2,c):
# def fun(a,b=2,c='3'):
#     print('a=',a,
#         'b=',b,
#         'c=',c,)

# fun(4)
# fun(1,b = 4)

################################################################################################################################
#全局变量,局部变量
################################################################################################################################
# APPLE = 5   #全局变量要大写
# a = None

# def fun():
#     # 如果要在函数里面改全局变量，使用global
#     # global a
#     a = 20
#     return a

# print(APPLE)
# print('a=',a)
# print(fun())
# print('a now=',a)

################################################################################################################################
# 读写文件
################################################################################################################################
# text = "this is my frist line\nthis is next line \nthis is last line"
# print(text)

# #重复写一个文件会覆盖
# my_file = open('my_file.txt','w')
# my_file.write(text)
# #操作文件后，要记得关上，不然要内存泄漏
# my_file.close()

# #追加
# append_text="\nThis is append_txt"
# my_file = open('my_file.txt','a')   #'a'表示追加
# my_file.write(append_text)
# my_file.close()

# #读取
# file = open('my_file.txt','r')
# #读单行
# # content = file.readline()
# # second_content = file.readline()
# #读全部行
# all_content = file.readlines()
# # print(content)
# # print(second_content)
# print(all_content)

################################################################################################################################
# 类
################################################################################################################################
#类名大写开头
# class Calculate:
#     #成员变量
#     name = 'zhangiang'
#     #函数每次参数self必不可少
#     def intruduce(self):
#         #用本类的成员变量要使用self
#         print(self.name)

#     def add(self,x,y):
#         reslut = x + y
#         print(reslut)
#     #类init功能（可以带默认值）
#     def __init__(self,name,price,high=18,width=20,weight=12):
#         # self.name = name
#         self.price = price
#         self.h = high
#         self.w = width
#         self.we = weight

# # c = Calculate('zl',12,3,4,54)
# c = Calculate('zl',12)
# print(c.name,c.price,c.h,c.w,c.we)
# calcul = Calculate()
# calcul.intruduce()
# calcul.add(1,3)
################################################################################################################################
#输入
################################################################################################################################
# a_input = input('please input a number:')  #返回是string
# if a_input == '1':
#     print('this is 1')
# elif a_input == '2':
#     print('this is 2')
# else:
#     print('good luck')
################################################################################################################################
# 元组
# a_tuple = (1,2,3,4,5,6)
# another = 3,4,5,6,7
# for i in range(len(another)):
#     #print(i)
#     print(i,'number in another=',another[i])

# #列表（和元组区别：可以使用append等操作）
# a_List = [1,2,3,4,5,2,4,3,5]
# a_List.append(10)
# #remove 不是按下标列，而是按原素的值，只删去第一个，后面的还保留
# a_List.remove(2)
# print(a_List)
# #打印最后1位
# print(a_List[-1])
# # : 从哪儿到到哪儿
# print(a_List[:3])
# print(a_List[4:])
# print(a_List[-2:])
# # 打印数字的索引（第一次出现）
# print(a_List.index(4))
# # 打印数字出现的次数
# print(a_List.count(4))
# 从小到大排序
# a_List.sort()
# print(a_List)
# # 从大到小
# a_List.sort(reverse=True)
# print(a_List)
################################################################################################################################
#字典
################################################################################################################################
#删除字典
# d = {'apple':1,'pear':2,'orange':3}
# print(d)
# del d['pear']
# print(d)
# #加入字典（不会按顺序）
# d['grape'] = 4
# print(d)
#字典内容可以是列表、字典，函数
# def fun():
#     print("in dict print")
#     return 1

# d = {'apple':[1,2,3],'pear':{1:3,2:'a'},'orange':fun()}

# print(d)
# print(d['pear'][1])
################################################################################################################################
# import导入模块
################################################################################################################################
# import time
# print(time.localtime())

#把引入库简写
# import time as t
# print(t.localtime())

#只引用库中部分内容,在代码中调用，不用再写库文件了
# from time import time,localtime
# #不用再写库名time了
# # print(time.localtime())  #编译报错
# print(time())
# print(localtime())

#只引用库中所有内容,在代码中调用，不用再写库文件了
# from time import *
# print(localtime())

#如果要使用自己写的模块：
# 1. 把模块放到和使用py同级的目录
# 2. 把模块放到使用编译python的默认py库中

################################################################################################################################
#异常报错
################################################################################################################################
# try:
#     file = open('test.txt','r')
# #接受错误存储在e变量中
# except Exception as e:
#     print('there is no file named as test.txt')
#     respone = input('Do you want create new file?')
#     if respone == 'Y' or respone == 'y':
#         file = open('test.txt','w')
#     else:
#         pass
# else:
#     print('open file success')

# file.close()
################################################################################################################################
#zip  ,map
# a = [1,2,3]
# b = [4,5,6]
#只能打印出对象地址
# print(zip(a,b))
# 元素位置合并[(1, 4), (2, 5), (3, 6)]
# print(list(zip(a,b)))
# 可以合并多个元素
#print(list(zip(a,a,b)))
# for i,j in zip(a,b):
#     print(i,j)
################################################################################################################################
#lambda 匿名函数
# fun = lambda x,y: x+y
# print(fun(2,3))
#map
# def fun2(x,y):
#     return x+y
# #参数在[]中，调用1+20 = 21
# print(list(map(fun2,[1],[20])))
# #输入多个参数,分开计算
# print(list(map(fun2,[1,4],[20,6])))
################################################################################################################################
#浅复制 & 深复制
################################################################################################################################
# a = [1,2,3]
# b = a
# #直接赋值，只是名字变幻下，指向存储地址一样（可以通过id查看）
# #修改b 也会影响到a
# print('ID_A='id(a),'ID_B=',id(b))

#浅copy,修改c内容不会影响到a
# import copy
# a = [1,2,3,[4,5]]
# c = copy.copy(a)
# c[1]=5
# print(a,'A_ID=',id(a))
# print(c,'C_ID=',id(c))
# #但是如果修改c中列表内容，如下： a的列表也还是被修改
# c[3][0] = 111
# print(a,'A_ID=',id(a))
# print(c,'C_ID=',id(c))

#深copy, 完全2个对立内存，互不影响
# import copy
# a = [1,2,3,[4,5]]
# e = copy.deepcopy(a)
# e[3][0] = 111
# print(a,'A_ID=',id(a))
# print(e,'C_ID=',id(e))

################################################################################################################################
# 多线程在1个核并行， 多个核之间并行
################################################################################################################################
################################################################################################################################
# pickle
# import pickle

# a_dict = {'da':1,2:"eref",4:'56'}
# #使用 with as file方式，不用file.close()较方便
# with open('pickle.pickle','wb') as file:
#     pickle.dump(a_dict,file)

# with open('pickle.pickle','rb') as file:
#     temp = pickle.load(file)
# print(temp)

################################################################################################################################
#set
# char_list = {'a','a','b','b','b','c','c','c'}
# print(set(char_list))
# sentence = 'welcome to New York'
# #注意空格，大小写都有区分
# print(set(sentence))
# #增加
# list2 = set(char_list)
# list2.add('x')
# # #清除
# # list2.clear()
# #删除
# list2.remove('a')
# #如果set里面没有值，remove会报错，运行不了，所以使用discard
# list2.discard('h')
# print(list2)
#显示不同的内容
# list1 = set(char_list)
# list3 = ['a','e','c']
# print(list1.difference(list3))
# #显示相同内容
# print(list1.intersection(list3))
################################################################################################################################
# 正则表达式
################################################################################################################################
# import re
# p1 ='cat'
# p2 = 'bird'
# string = 'dog runs to cat'
# print(re.search(p1,string))
# print(re.search(p2,string))
# #匹配a,u 2种情况
# p3 = r"r[a|u]n"
# print(re.search(p3,string))
#匹配多种
# p4 = r"r[A-Z]n"
# p5= r"r[0-9A-Z]n"
# string2 = 'dog r2ns to cat'
# print(re.search(p5,string2))

# print(re.search(r'cats$',"dog runs to cats"))

# print(re.search(r'Mon(day)?',"Monday"))
# print(re.search(r'Mon(day)?',"Mon"))

# string = """
# dog ran to cat.
# I ran to dog.
# """
# print(re.search(r'^I',string))
# print(re.search(r'^I',string,flags=re.M))

# print(re.search(r'ab{2，3}',"ab"))   #匹配不到,匹配b出现2到3次
# print(re.search(r'ab{2,10}',"abbbb"))  #匹配成功


# match = re.search(r'(?P<id>\d+), Date: (?P<date>.+)',"ID:201512, Date: Feb/12/2018")
# print(match.group())  #全部打印
# print(match.group('id'))  #打印第一个
# print(match.group('date'))  #打印第2个

# print(re.sub(r'r[a|u]ns','catches',"dog runs to cat"))
# print(re.split(r'[,;\\.]',"a;b,c.d\e"))
################################################################################################################################