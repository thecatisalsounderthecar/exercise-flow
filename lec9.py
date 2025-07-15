# # test例题-闭包
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
 
# times3 = make_multiplier_of(3)
# times5 = make_multiplier_of(5)
 
# print(times3(9))
# print(times5(3))
# print(times5(times3(2)))

# # ex例题-文件读取
# from pathlib import Path
# path=Path('testlec9.txt')
# try:
#     contents=path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f'The file {path} is not found.')
#     # 注意这里是f不是r，几种前缀的区别见笔记
# else:
#     words=contents.split()
#     num_words=len(words)
#     print(f'There are {num_words} words in this text.')

# # ex例题：Json写入&读取
# from pathlib import Path
# import json

# numbers=[2,3,5,7,11,13]

# path=Path('numbers.json')
# contents=json.dumps(numbers)#内容写入字符串
# # 注意是dumps不是dump,不加s括号里得跟文件地址，加s括号里跟对象
# # 这步转换出来的json是'[2,3,5,7,11,13]'，是json里的数组类型
# path.write_text(contents)#字符串写入文件

# contentr=path.read_text()#从json文件读入内容
# numbersr=json.loads(contentr)
# # 注意是loads不是load
# print(numbersr)

# ex例题-用户名写入读取打招呼
from pathlib import Path
import json

path1=Path('testjson.txt')
def get_stored_username(path):
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    username=input('What\'s your user name?')
    contents=json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path=Path('username.json')
    username=get_stored_username(path)
    if username:
        print(f'Welcome back,{username}!')
    else:
        username=get_new_username(path)
        print(f'We\'ll remember you when you come back,{username}!')

greet_user()


