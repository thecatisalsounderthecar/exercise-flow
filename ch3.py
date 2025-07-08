names=['jcx','ftx','wyt']
# 3.1
# print(names)

# 3.2
# print(names[0]+',good morning!')
# print(names[1]+',good morning!')
# print(names[2]+',good morning!')

# 3.3
# 略

# 3.4略
# 3.5
invitation=['jcx','ftx','wyt','wjy']
# print (invitation)
# absent='wyt'
# print(absent)
# inx=invitation.index(absent)
# invitation.remove(absent)
# invitation.insert(inx,'sb.new')
# print (invitation)

# # #3.6
# print('A bigger dining table has been found！')
# invitation.insert(0,'ben')
# invitation.insert(inx+1,'edd')
# # invitation.insert(-1,'phil')
# invitation.append('may')
# print(invitation)

# #3.7
print('Latest news:only two guests can be invited due to the delay of logistics.')
while len(invitation)>2:
    abguest=invitation.pop()
    print (abguest+',I\'m sorry that I can\'t invite you!')
# 3.9
print(str(len(invitation))+' guests are invited.')
print(invitation[0]+',You are still invited.')
print(invitation[1]+',You are still invited.')
del invitation[0]
# 第二个元素也是del invitation[0]是因为第一个删掉后第二个变成第一个
del invitation[0]
print(invitation)


# 3.8
destination=['British','Estonia','Russia','Holland','New Zealand']
print(destination)
print(sorted(destination))
print(destination)
# true记得大写，不然解释器看不懂
# sorted参数可以熟悉一下
print(sorted(destination,reverse=True))
print(destination)
destination.reverse()
print(destination)
destination.reverse()
print(destination)
destination.sort()
print(destination)
destination.sort(reverse=True)
print(destination)



