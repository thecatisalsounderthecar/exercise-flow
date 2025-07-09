# # Lec4 PPT例题 简易记账本

# # 账本数据结构：列表，每个列表元素是如下字典
# # 【key】rdate-【value】int类型
# # 【key】(type)a|b|c|… -【value】a累计金额|b累计金额|c累计金额|…
# # 直接将具体类型作为键，金额作为type的值，不一定是json那样的type字段名->type字段值->amt字段名->amt值的结构
# # 注意字典和json区别：字段值直接作为索引

# # 否则的数据结构：
# # rdate:XX
# # data:{
# #     type:a/b/c/d
# #     amt:XX
# # }

# # 初始化
# print('简易记账本（July）\n')#单引号和双引号在定义字符串时没区别，只有字符串里包含单引号双引号时可以避免转义的区别
# July=[]
# for rdate in range(0,31):
#     July.append({})

# # 用户输入日期
# rdate=int(input('请输入记账日期：'))
# # July[rdate-1][rdate]=rdate
# # 上面这句比较多余，会存{"3":"3"}这种键值对

# # 用户输入记账
# while True:
#     amt=int(input('请输入记账金额,结束输入0：'))
#     # 这里将输入0同时作为金额和退出标志，一方面是保证输入为0的时候金额总计不变，另一方面起到退出标志的作用
#     if amt==0:
#         break
#     else:
#         type=input('请输入记账类型：a.衣 b.食 c.住 d.行 e.其他  ')
#         July[rdate-1][type]=July[rdate-1].get(type,0)+amt
#         print("记录成功！")
#         # July[rdate-1][type]=July[rdate-1][type]+amt
#         # 变量名写July[rdate][cashflow]不行，可能是因为amt没有声明
#         # 不用get方法也不行，没法初始化为0，放别的地方赋值=0初始化逻辑更不对

# # 按类型查询
# typecon=input("请输入查询类型：")
# print(July[rdate-1].get(typecon,0))
# # 注意这里get()的第一个参数是键值，不要打成[typecon]，这表示拿一个列表作为键值去查询，显然不行


# # Lec5 PPT例题 情感分析
# text='This movie was absolutely amazing! The story was engaging\
#  and the characters were great. However, some scenes felt unnecessary\
#  and a bit boring. Overall, I loved it!'
# text=text.lower()

# clean_string=""
# for char in text:
#     if char.isalpha() or char.isspace():
#         #上一行不要写成text.isalpha，检查的每个单位是char不是原始文本
#         clean_string+=char
# words=clean_string.split()#.split()输出自动是列表型

# good=['amazing','engaging','great','love','loved']
# bad=['boring','unnecessary']

# goodcnt=0
# badcnt=0
# for word in words:
#     if word in good:
#         goodcnt+=1
#     elif word in bad:
#         badcnt+=1
#     else:
#         pass

# print(f'正向词汇共{goodcnt}个，负向词汇共{badcnt}个')
# if goodcnt>badcnt:
#     print(f'文本为正向描述')
# elif goodcnt<badcnt:
#     print(f'文本为负向描述')
# else:
#     print('文本无正负偏向')


# # ch6
# # 6.1,6.7
# info1={"name":"laoyu","age":"24","city":"edinburgh"}
# info2={"name":"ben","age":"45","city":"london"}
# info3={"name":"river","age":"28","city":"london"}
# profile=[info1,info2,info3]
# print(profile)

# # 6.2
# likenum={
#     "laoyu":2,
#     "laofang":3,
#     "laowang":4,
#     "laoji":5,
# }
# print(likenum)

# # 6.3,6.4
# vocabulary={
#     "language":"python",
#     "string":"a type of data",
#     "int":"integer",
#     "dictionary":"a data type peculiar to python"
# }
# vocabulary["str"]="string"

# for key,inter in vocabulary.items():#这个括号不要忘加，方法一般都是需要空括号的
#     print(f"term:{key}"+f" ; interpretation:{inter}")

# # 6.6
# interview=["laofang","laoyu","laowang2","laogen"]
# for interviewee in interview:
#     if likenum.get(interviewee):
#         print(f"{interviewee},thanks for taking part!")
#     else:
#         print(f"{interviewee},please take part!")


# 6.9
# 注意列表键值唯一
# favorite_places={
#     "dingding":["italy","spain","japan"],
#     "fish":["england"],
#     "JJ":["japan"]
# }

# for person in favorite_places.keys():
#     personplace=[]
#     personplace.extend(favorite_places.get(person))
#     print(f"{person}'s favorite places are:")
#     print(personplace)

# 6.11
cities={
    "shanghai":{"country":"china","population":"10k","fact":"oriental pearl tv tower"},
    "london":{"country":"england","population":"12k","fact":"old-school"},
    "newyork":{"country":"USA","population":"8k","fact":"highly-developed finance industry"}
}
for cityname in cities.keys():
    ct=cities[cityname].get("country")
    print(f"{cityname}'s country is:{ct}")
    pop=cities[cityname].get("population")
    print(f"{cityname}'s country is:{pop}")
    fac=cities[cityname].get("fact")
    print(f"{cityname}'s country is:{fac}")
