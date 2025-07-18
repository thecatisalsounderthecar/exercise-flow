import numpy as np
# a=np.array([[1,2,4,4],[4,4,5,6]])
# print(a)
# print(np.sum(a,axis=0))

# b=np.array([[1,3,6],[9,3,2],[1,4,3]])
# print(np.where(b>3,520,1314))
# print((b>3).all())#输出False
# print(np.any(b>3))#输出True
#输出[ 5  6  9 10]
# print(np.cumsum(a))
# print('平均值：')
# print(np.mean(a))
# print('加权平均值：')
# print(np.average(a))
# counts=np.bincount(a)
# most=np.argmax(counts)
# print(counts)
# # 输出[0 1 1 0 4 2 1],分别对应整数0-6=amax，所以argmax读索引等价于读出原整数众数
# print(most)
x1=np.array([[0,12,48],[4,18,14],[7,1,99]])
a1=np.sort(x1)
print(a1)

x2=np.array([[0,12,48],[4,18,14],[7,1,99]])
print(np.array([np.take(x2[i],x2[i].argsort())for i in range(3)]))