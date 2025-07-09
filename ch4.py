# # 4.1
# pizzas=['sausage','mushroom','salami']
# for pizza in pizzas:
#     print (f'I like {pizza} pizza')
# print('I really love pizza!')
# friend_pizzas=pizzas[:]
# pizzas.append('royal')
# friend_pizzas.append('shrimp')
# for pizza in pizzas[:]:
#     print(pizza)
# for fpizza in friend_pizzas[:]:
#     print(fpizza)
# # 4.2
# cats=['Chinese Lihua','Lion','tiger']
# for cat in cats:
#     print(f'A {cat} would make a great pet(?)')
# print('Not all cats would make goood pets!')

# #4.3
# for value in range(1,21):
#     print(value)

#4.5
# values=[value for value in range(1,1000001)]
# minimum=min(values)
# maximum=max(values)
# s=sum(values)
# print(s)

# #4.6
# values2=list(range(1,21,2))
# for value2 in values2:
#     print(value2)

# #4.7
# values3=list(range(3,31,3))
# for value3 in values3:
#     print(value3)

# #4.8
# trips=[value**3 for value in range(1,11)]
# for trip in trips:
#     print(trip)
# print('The first three items in the list are:')
# for trip in trips[1:4]:
#     print(trip)
# print('Three items in the list are:')
# for trip in trips[3:6]:
#     print(trip)
# print('The last three items in the list are:')
# #注意不是[-3,-1]，这样是-3和-2输出
# for trip in trips[-3:]:
#     print(trip)
# # 4.9 同4.8

# 4.13
foods=('macroni','sphagetti','noodles','pasta','cream')
for food in foods:
    print(food)
foods=('alt1','alt2','noodles','pasta','cream')
for food in foods:
    print(food)