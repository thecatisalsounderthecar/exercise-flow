# # PPT例题1：创建狗对象
# class Dog():
#     def __init__(self,name,age):
#         # init双下划线
#         self.name=name
#         self.age=age

#     def sit(self):
#         print(f"{self.name} is now sitting.")
    
#     def roll_over(self):
#         print(f"{self.name} rolled over!")

# my_dog=Dog('Willie',6)
# print(f"My dog\'s name is {my_dog.name}.")
# print(f"It is {my_dog.age} years old.")

# my_dog.sit()
# my_dog.roll_over()

# # PPT例题2：创建车对象
# class Car():
#     # 创建对象时一定不传入参数，到init中才传递
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0
    
#     def get_descriptive_name(self):
#         # 传入参数只要self即可，剩下三个其属性自己跟着进来了
#         long_name=f"{self.make} {self.model} {self.year}"
#         return long_name
#     # 这里不直接用print，可能是希望对该名字后续做运算。

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def increment_odometer(self,inc):
#         self.odometer_reading+=inc
        

# my_new_car=Car('Audi','A4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# my_new_car.odometer_reading=23
# my_new_car.read_odometer()

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

# class  Electric_car(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         # 敲到def __init__ 后按tab自动会把super那一句也补全
#         self.battery_size=70

#     def describe_battery(self):
#         print(f"loaded with {self.battery_size}-kwh battery.")

# class Fuel_car(Car):
#     pass

# class old_car(Car):
#     def __init__(self, make, model, year):
#         Car.__init__(self,make, model, year)
#         # 注意self也要传入，不然会报错少最后一个参数

# my_tesla=Electric_car('Tesla','model s',2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

# my_aston=Fuel_car('Aston Martin','Valkyrie',1990)
# print(my_aston.get_descriptive_name())

# Coulson_Lola=old_car('Audi','red prototype',1920)
# print(Coulson_Lola.get_descriptive_name())

# stuff = []
# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
 
# print(stuff[0])
# print(stuff.__getitem__(0))
# print(list.__getitem__(stuff,0))
import numpy as np
def add(n):
    a=np.arange(1,n+1)**3
    b=np.arange(1,n+1)**2
    return a+b
print(add(3))