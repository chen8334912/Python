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