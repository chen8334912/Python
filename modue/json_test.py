'''''

# dic = str({'name':'alex','age':'18'})
# f = open('hello' , 'w')
# f.write(dic)

# f_read = open('/Volumes/Work/Python/hello','r')
# data = f_read.read()
# print(data,type(data))
# data = eval(data)     #eval函数就是实现list、dict、tuple与str之间的转化, str函数把list，dict，tuple转为为字符串
# print(data['name'])



import json

# dic = {'name' : 'chris'}          # ---->>'{"name": "chris"}'
# dic1 = 8          # ---->>'8'
# dic2 = 'hello'          # ---->>' "hello" '
# data = json.dumps(dic)      # json.dumps()用于将dict类型的数据转成json标准的str类型，因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。
#
# print(data, type(data))
#
# f = open('new_hello', 'w')
# f.write(data)

# f_read = open('new_hello', 'r')
# data = f_read.read()
# print(data, type(data))
#
# data2 = json.loads(data)       # json.dumps()用于将将str类型的数据转成dict类型。
# print(data2, type(data2))
# print(data2['name'])




#----------------------------序列化
import json

dic={'name':'alvin','age':23,'sex':'male'}
print(type(dic))#<class 'dict'>

j=json.dumps(dic)    
print(type(j))#<class 'str'>


f=open('序列化对象','w')
f.write(j)  #-------------------等价于json.dump(dic,f)
f.close()
#-----------------------------反序列化<br>
import json
f=open('序列化对象')
data=json.loads(f.read())#  等价于data=json.load(f)


'''''

'''''

import pickle         # 使用pickle读写文件都要用'b'('rb','wb'),而json都用't'('rt','wt')

# dic={'name':'alvin','age':23,'sex':'male'}
# with open('hello' , 'wb') as f:
#     pickle.dump(dic, f)

with open('hello' , 'rb') as f:
    data = pickle.load(f)
    print(data)


'''''