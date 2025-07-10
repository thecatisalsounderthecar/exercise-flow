# # lec6 PPT例题 21点游戏
# import math
# import random

# def create_deck():
#     singlev=[2,3,4,5,6,7,8,9,10,10,10,11]
#     deck=singlev*4
#     random.shuffle(deck)
#     #shuffle函数原地打乱，所以其实这里不用再把打乱完的结果赋值给别的变量，原地输出即可
#     return deck

# def calculatepoints(card):
#     tp=sum(card)
#     acen=card.count(11)
#     while tp>21 and acen >0:
#         tp-=10
#         acen-=1
#     return tp
# # 我不太懂为什么会有A从11到1的分数转化，反正先这么写了

# def player_round(pcard,deck):
#     call=input("是否叫牌？y/n")
#     if call=='y':
#         pcard.append(deck.pop())
#         # 注意deck不能跨函数直接调用，要用得从参数传入
#     else:
#         pass
#     pscore=calculatepoints(pcard)
#     print(f'玩家回合结束，目前分数为{pscore}')
#     return pscore,deck
#     # deck要实现动态变化，也需要返回

# def dealer_round(dcard,deck):
#     dscore=calculatepoints(dcard)
#     if dscore<17:
#         dcard.append(deck.pop())
#     return dscore,deck

# def main():
#     print('游戏开始，第一轮发牌')
#     deck=create_deck()
#     # pcard=[]
#     # dcard=[]
#     # pcard.append(deck.pop(),deck.pop())
#     # dcard.append(deck.pop(),deck.pop())
#     # 错误写法，append只能有一个参数
#     pcard=[deck.pop(),deck.pop()]
#     dcard=[deck.pop(),deck.pop()]
#     # 玩家回合
#     playerscore,deck=player_round(pcard,deck)
#     print('玩家分数：')
#     print(playerscore)
#     print('玩家手牌：')
#     print(pcard)
#     # 庄家回合
#     dealerscore,deck=dealer_round(dcard,deck)
#     print('庄家分数：')
#     print(dealerscore)
#     print('庄家手牌：')
#     print(dcard)
#     if playerscore>=21:
#         print('玩家爆牌，庄家胜！')
#     elif dealerscore>=21:
#         print('庄家爆牌，玩家胜！')
#     elif playerscore<21 and dealerscore<21 and playerscore>dealerscore:
#         print('玩家点数大，玩家胜！')
#     elif playerscore<21 and dealerscore<21 and playerscore<dealerscore:
#         print('庄家点数大，庄家胜！')

# main()

# ch8
# 8.4
# def LT(size='L',caption='I LOVE PYTHON'):
#     print(f"size:{size},caption:{caption}")

# LT('M')

# # 8.7,8.8
# def make_album(singer,albumn,songnum=''):
#     albuminfo={"singer":singer,"album":albumn}
#     if songnum:
#         albuminfo["songnumber"]=songnum
#     print(albuminfo)

# while True:
#     isinger=input('请输入歌手名：')
#     ialbumn=input('请输入专辑名：')
#     exit=int(input('输入结束请按0。'))
#     if exit==0:
#         # 判断条件如果写exit==0就不对了，因为input输入是字符串类型
#         make_album(isinger,ialbumn)
#         break
#     else:
#         isongnum=input('请输入歌曲数（可选）：') 
#         make_album(isinger,ialbumn,isongnum)
#         break  

# 8.9-8.11
# inputlist=['hello world!','good morning!','what\'s that?']
# def show_messages(ilist):
#     for message in ilist:
#         print(message)
# show_messages(inputlist)

# def send_messages(ilist):
#         global send_message
#         send_message=[]
#         for message in ilist:
#             print(message)
#             send_message.append(message)

# inputlistcopy=inputlist[:]
# send_messages(inputlistcopy)
# print(inputlist)
# print(send_message)

# # 8.12
# def sandwich(*toppings):
#     print('The ingredients of this sandwich are:')
#     for topping in toppings:
#         print(topping)

# sandwich('sausage')
# sandwich('sausage','vegetables','cheese')

# 8.13
def build_profile(*name,**info):
    print('name:')
    for subname in name:
        print(subname+' ')
    personnelprofile={}
    for k,v in info.items():
        # 括号又忘写了
        personnelprofile[k]=v
    print(personnelprofile)

build_profile('river','cartwright',location='slough house',state='active',type='field agent')

