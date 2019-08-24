# class Name:
#     def gan():
#         print('ksldjf')
#     def gang(self):
#         print('123123')
#
# p1 = Name()
# print(p1.gang())
# print(Name.gan())

# coutry = 'USA'
# class Chinese:
#     coutry = 'China'
#     l = [1,2]
#     def __init__(self,name):
#         self.name = name
#         print(coutry)
#
# p1 = Chinese('alex')
# print(p1.coutry)
# print(Chinese.coutry)
# print(p1.l)
# p1.l = [1,2,3,4]     # 修改的对象的属性，等于给p1新增了一个l的属性
# print(p1.l)
# p1.l.append(5)      # 修改的类的属性


'''''

#------------>>>>>>>实例方法,直接用实例去调用,只要方法里有self就可以断定是实例方法

class  Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def __str__(self):
        return ("{year}-{month}-{day}").format(year=self.year,month=self.month,day=self.day)

    def yesterday(self):
        self.day-=1

date=Date(2018,10,20)
print(date)

date.yesterday()

print(date)


'''''


'''''


class  Date:
    day=10   #添加 类属性 day
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def __str__(self):    
        return ("{year}-{month}-{day}").format(year=self.year,month=self.month,day=self.day)

    def yesterday(Date):
        Date.day-=1         #对类进行修改， 记住用的是Date.day ,如果是实例方法必须是 self.

date=Date(2018,10,20)
print(date)
#打印结果    实例传入 day =20， 就用实例的20，不会找 类的a=102018-10-20
Date.yesterday(Date)
print(date)
#打印结果 如下， 这个全部用的是类，跟self 没有关系，所以还是打印结果不变。2018-10-20
print(Date.day)
#打印结果  调用修改类属性方法 生效。  如果self 没有day 这个属性，他一定去找类的变量 day， 这个可以自己尝试下。9

'''''


'''''

#------------>>>>>>>静态方法用 @staticmethod 标识

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return ("{year}-{month}-{day}").format(year=self.year, month=self.month, day=self.day)

    def yesterday(Date):
        Date.day -= 1

    @staticmethod       #  用这个装饰器表明是静态方法，这个要注意。
    def static(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))


new_day=Date.static("2018-10-10")    #由于静态方法不属于实例 所以调用的时候， 用类名.静态方法，这个要注意
print(new_day)


#打印结果  正好是咱们的预期结果。2018-10-10



'''''


'''''

#------------>>>>>>>类方法同样也有装饰器用 @classmethod ，实例方法传递的是self，类同样也是对象直接传递cls就行

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return ("{year}-{month}-{day}").format(year=self.year, month=self.month, day=self.day)

    def yesterday(Date):
        Date.day -= 1

   # @staticmethod
    #def static(date_str):
     #   year, month, day = tuple(date_str.split("-"))
      #  return Date(int(year), int(month), int(day))

    @classmethod       #类方法的标识
    def class_method(cls,date_str):    # 这个cls只是表明类对象，是可以修改的，同样你改为self也是一样，叫cls为了提高可读性。
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))         #这个cls 和上边是一样的意思，这个就比静态方法好处就是会随便类名变化而变化。

new_day=Date.class_method("2018-10-10")
print(new_day)
#打印结果 2018-10-10

'''''

'''''


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return ("{year}-{month}-{day}").format(year=self.year, month=self.month, day=self.day)

    def yesterday(Date):
        Date.day -= 1

    @staticmethod     #校验输入值类型和大小是否符合咱们的类型。
    def var_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if 0 < int(year) and 0 < int(month) <= 12 and 0 < int(day) < 32:
            return True
        else:
            return False

    @classmethod
    def class_method(cls, date_str):

        if cls.var_str(date_str):  #这里是调用静态方法，注意要用cls.静态方法，原理和实例方法中的self一样，自己可以试试，否则是不能读取的。
            year, month, day = tuple(date_str.split("-"))
            return cls(int(year), int(month), int(day))


new_day = Date.class_method("2018-10-10")
print(new_day)
# 打印结果 2018 - 10 - 10


'''''

'''''


class Vehicle:
    Country = 'China'
    def __init__(self,name,speed,load,power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('开动啦')
        print('开动啦')

# class Subway(Vehicle):
#     def __init__(self,name,speed,load,power,line):
#         Vehicle.__init__(self.name,self.speed,self.power)
#         self.line = line
#
#     def show_info(self):
#         print(self.name,self.speed,self.load,self.power,self.line)
#
#     def run(self):
#         Vehicle.run(self)
#         print('%s %s 线, 开动啦' %(self.name,self.line))
#
#
# line13 = Subway('北京地铁','10000km/s',1000000,'电',15)
# lin13.show_info()
# line13.run()



print(Vehicle.Country)
v1 = Vehicle('北京地铁','10000km/s',1000000,'电')
# v1 = Vehicle()
# print(v1.name)



'''''

'''''

class People:
    _star = 'fuck'
    __star = 'earth'
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def get_id(self):
        print('我是私有方法，我找到的id是%s' %self.id)
        
    # 访问函数,通过类内部去调用自己的方法
    def get_star(self):        
        print(self.__star)

p1 = People(1048,'chris',32)
print(p1._star)
print(People.__dict__)
print(p1._People__star)
p1.get_star()



'''''

'''''
#------>>  动态导入模块

from m1.t import *
test1()
test2()
# _test3()        # 使用了封装的函数，在用*的情况外部是调用不到函数的


s = __import__('m1.t')
print(s)
s.t.test1()
s.t.test2()
s.t._test3()

import importlib

w = importlib.import_module('m1.t')
print(w)
w.test1()
w.test2()
w._test3()


'''''



class Foo:
    x = 1
    def __init__(self,y):
        self.y = y

    def __getattr__(self, item):        #self为实例对象，item为调用的属性
                                        # __getattr__只有在使用点调用属性且属性不存在的时候才会触发
        print('触发__getattr__---->你要调取的属性【%s】不存在'%item)

    def __delattr__(self, item):        #__delattr__删除属性的时候会触发
        print('触发__delattr__---->删除了相关属性')

    def __setattr__(self, key, value):  #__setattr__添加/修改属性会触发它的执行
        print('触发__setattr__---->修改了相关属性')    # 因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,
                                                      # 就是根本没赋值,除非你直接操作属性字典,否则永远无法赋值
        self.__dict__[key] = value


f = Foo(2)       #实例化相当于赋值操作，则触发__setattr__
f.z = 3          #增加z属性，则触发__setattr__
print(f.y)     #2
f.yyyy         #触发__getattr__---->你要调取的属性【yyy】不存在

del f.x        #触发__delattr__---->删除了相关属性



'''''


class Foo:
    x = 1
    def __init__(self,y,tag = False):
        self.y = y
        self.tag = tag

    def __getattr__(self, item):        #self为实例对象，item为调用的属性
                                        # __getattr__只有在使用点调用属性且属性不存在的时候才会触发
        print('触发__getattr__---->你要调取的属性【%s】不存在'%item)

    def __delattr__(self, item):        #__delattr__删除属性的时候会触发
        if self.tag == True:                    #可用来判断用户是否有权限删除属性
            print('已经删除属性【%s】'%item)
            self.__dict__.pop(item)
        else:
            print('无权限删除')

    def __setattr__(self, key, value):  #__setattr__添加/修改属性会触发它的执行
            if type(value) is str:          #可用来判断用户设置的属性是否是指定的类型
                print('已将【%s】属性设置为【%s】'%(key,value))
                self.__dict__[key] = value
            else:
                print('设置的属性不合法！')

f = Foo(2)

# 1 可以用__getattr__来提示用户调用的属性不存在，而不是直接报错
print(f.z)                      #触发__getattr__---->你要调取的属性【z】不存在

# 2 可以用__delattr__来根据用户权限来是否执行删除操作，可以保护类的属性
f1 = Foo(3)
del f1.y                        #因为f1实例没有传入tag权限属性值      ---> 无权限删除
print(f1.__dict__)              #{'y': 3, 'tag': False}
f2 = Foo(4,True)                #传入了tag权限为True，所以可以执行删除操作
del f2.y                        #已经删除属性【y】
print(f2.__dict__)              #{'tag': True}

# 3 可以用__setattr__来规范用户传值类型
f3 = Foo('5')                   #已将【y】属性设置为【5】



'''''