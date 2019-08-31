import numpy as np
from pandas import Series
from pandas import DataFrame
from  pandas import read_csv
from  pandas import read_excel
from  pandas import read_table



# data1 = [1,2,3,4,5,4.5]
# data2 = [[1,2,3],[4,5,9]]


'''''

# --------->>>>>>数据类型转换



array1= np.array(data1)
array2= np.array([1,2,3,4,5,'4.5'])
array3= np.array(data2)




# 数据类型转换
# array25 = array1.astype(np.float)
# array25 = array1.astype(np.int)     #如果讲浮点数转换成整数，则小数部分被截断
# array25 = array1.astype(np.string_)     # 字符串数组可以转换成数值型
# array25 = array1.astype(np.str)
# array5 = array2.astype(np.float)      # 数值型转换成浮点型



print(array1)
print(type(array1))
print(array1.dtype)
print(array3,type(array3),array3.dtype)
# print(array25)
# print(array25.dtype)
print(array5)
print(array5.dtype)

'''''

'''''

array1= np.array(data1)
array2= np.array([1,2,3,4,5,'4.5'])
array3= np.array(data2)


# --------->>>>>>数组内计算

# print(array1 + 1)
# print(array2.astype(np.float) + 1)         # 数值型转换成浮点型进行计算
# print(array3 + 1)

# --------->>>>>>数组内索引
array1[1] = 14                     #数组内元素替换
print(array1[1],array1[-2:])
print(array3[1],array3[1][1])



'''''


'''''
# --------->>>>>>Pandas有Series和Dataframe两种数据结构

d1= Series([2,2.4,'ab'],index = [2,1,3])
d2= Series([2,2.4,'ab','jksdljf'],index = ['a','b','c','e'])
# print(d1)
# print(d2)
# # print(d1.dtype)
# s2 = d2['b']
# print(s2)

# 追加一个系列，不能单独追加元素
d3 = d2.append(Series(['chifan'],index=['d']))
print(d3)

# # 判断值是否存在，数字型和逻辑型(True/False)不需要加引号
# print('chifan' in d3.values)
# print(2.4 in d1.values)
#
# print(d2[1:3])
# print(d2[3])            # 根据索引号访问
# print(d2.index[0])       # 根据索引号查找索引名
# print(d2[[1,3,2]])      # 随机抽样会用到

# d4 = d3.drop('e')      # 按索引名删除
# d4 = d3.drop(d3.index[2])      # 根据索引号删除
# d4 = d3[2.4 != d3.values]      # 根据值删除


# 根据值查找系列index
# d4 = d3.index[d3.values == 'chifan']
# print(d4)


# # 修改序列的值
# print(d3.values ==2.4)
# print(d3.index[d3.values ==2.4])
# d3[d3.index[d3.values== 2.4]] = '2.5'
# print(d3)

# 修改Series中的index
# d3.index = [6,1,2,3,5]
# print(d3)
# print(d3[1:3])


'''''

'''''

# DataFrame数据框用于存储多行和多列的数据集合，是Series的容器

df  = DataFrame({
    'age':Series([26,29,33]), 'name':Series(['ken','chris','fish'])},index=[1,2,0])

print(df)


# 访问列，获取age列的值
# age = df['age']
# print(age)

# 访问行，获取索引号取对应行的值
# b = df[0:1]
# print(b)
# c = df[1:3]
# print(c)


# 访问块,从n行到m行（不含）与x列到y列（不含）的块
# b = df.iloc[0:2,0:2]
# print(b)


# 访问指定位置,n行与y列的交叉值
b = df.at[2,'name']
print(b)


'''''


# df1  = DataFrame({
#     'age':[26,29,33], 'name':['ken','chris','fish']})
#
# df2  = DataFrame(data = {
#     'age':[26,29,33], 'name':['ken','chris','fish']},index=['first','second','third'])
#
# print(df1)
# print(df2)

# 访问行
# print(df1[1:100])     # 显示为index = 1-99行的数据
# print(df1[-2:1])     # 显示为空
# print(df1[1:1])     # 显示为空
# print(df1[4:1])     # 显示为空
# print(df2['second':'second'])    #索引名访问单行
# print(df2['fist':'second'])    #索引名访问多行


# 访问列
# print(df1['name'])    #列名访问单行
# print(df1[df1.columns[0:2]])    #索引名访问多列


# 访问块
# print(df1.iloc[0:1,0:1])

# 访问位置
# print(df1.at[1,'name'])
# print(df2.at['first','name'])


# 修改列名
# df1.columns = ('age1','name1')
# print(df1)


# 修改行索引
# df1.index = range(2,5)
# print(df1)


# 根据行索引删除
# df3 = df1.drop(1,axis=0)     #  使用0值表示沿着每一列或行标签/索引值向下执行方法
# df3 = df1.drop('name',axis=1)     # 使用1值表示沿着每一行或者列标签横向执行对应的方法
# del df1['name']        # 另一种删除方式，在原数组上面删除
# print(df1)
# print(df3)


# 增加

# df1['sex'] = ['boy','girl','boy']           # 增加列方式，在原数组上面增加
# print(df1)


# df = DataFrame([[1,2,3],[3,4,5],[5,6,7]],columns=list('ABC'))
# df2= DataFrame([[11,22,33],[17,943,12],[17,943,12]],columns=list('ABC'))
# df3 = df.append(df2,ignore_index=True)    # 合并生成一个新的数据框，并产生新的index
#
# # df3 = df.append(df2)      # 叠加生成新的数据框，不修改index
# print(df3)
# # print(df3[3:5])





# df = read_csv(r'rz.csv',sep=',')
# print(df)

# df = read_excel(r'rz.xlsx',sheet_name='Sheet1',header=0)
# print(df)

# 查找是否有重复行
# print(df.duplicated('学号',keep='first'))

# 删除重复行
# df2 = df.drop_duplicates('学号')
# print(df2)

# 查找缺失数据
# print(df.isnull())
# print(df.notnull())

#删除缺失行
# df3 = df.dropna(how = 'all')   # 行里数据全为空的时候丢弃
# print(df3)

#删除缺失列
# df4 = df.dropna(axis=1)   #  axis=1是按列丢弃
# print(df4)

# 替换缺失值
# df4 = df.fillna('chris')
# df4 = df.fillna(method='pad')  # 用前一值替换缺失值NaN
# df4 = df.fillna(method='bfill')  # 用后一值替换缺失值NaN
# df4 = df.fillna(df.mean())  # 用平均数替换缺失值NaN
# df4 = df.fillna(df.mean()['高代':'解几'])    # '补全列名':'计算均值的列名'
# print(df4)






'''''

a = np.arange(100, dtype=float).reshape((10, 10))
for i in range(len(a)):
    a[i, :i] = np.nan
a[6, 0] = 100.0

d = DataFrame(data=a)
print(d)

# 连续空值，最多填补3个
# print(d.fillna(method='ffill',axis=0, limit=3))

# 每条轴上，最多填补3个
print(d.fillna(1,axis=0, limit=3))


'''''
'''''

# -------->>>> 字段抽取

df = read_excel('i_nuc.xls',sheet_name='Sheet4')


# print(df.head())
tel = df['电话'].astype(str)
print(tel)

print(tel.str.slice(0,3))
print(tel.str.slice(3,7))
print(tel.str.slice(7,11))


'''''
'''''

df = read_excel('i_nuc.xls',sheet_name='Sheet4')

# print(df['IP'])

# 删除首尾空格
# df2 = df['IP'].str.strip()

# 按'.'分3列
df3 = df['IP'].str.split('.',3,True)

# 增加列名称
df3.columns = ['IP_1','IP_2','IP_3','IP_4']

# print(df2)
print(df3)


'''''
'''''

df = DataFrame({'age':Series([22,34,56,23,12]),
                'name':Series(['Ban1','Ban2','Ban3','Ban4','Ban5'])})

# 以name列为新的索引
df1 = df.set_index('name')

# 重新建立从0开始的索引
df1 = df.reset_index(drop=True)
print(df)
print(df1)

print(df1.loc['Ban2'])      # 根据索引定位行
print(df1.iloc[3])      # 根据索引号定位行

'''''


'''''

df = read_excel('i_nuc.xls',sheet_name='Sheet4')
# print(df)

# print(df.astype(str))

#   记录抽取,条件完全符合
# df2 = df[df['电话'] == 19934210915.0]
# df2 = df[df.电话 == 19934210915.0]
# df2 = df[df.IP == 221/.205/.98/.55]  ?????????


# df2 = df[df['电话'] > 19934210915.0]
# df2 = df[df['电话'].between(19934210915.0,19934210918.0)]
# df2 = df[df.IP.isnull()]
# df2 = df[df.IP.str.contains('222',na = False)]
# print(df2.astype(str))

df2 = df.set_index('学号')
# print(df2.astype(str))
# print(df2.loc[2308024307:2308024310])     # loc通过索引去行数据,loc[行标签,列标签]
df3 = df2.loc[:,'电话'].head()     # 选取‘电话’列的数据
print(df3.astype(str))



'''''








# df = DataFrame({'a':[1,2,3,4,5,6],'b':['a','b','c','d','e','f'],'c':['A','B','C','D','E','F']})
# print(df)
# print(df.loc[1])   # 抽取 index = 1 的行，但返回的是Series，而不是DataFame
# print(df.loc[[1,2]])   # 抽取 index= 1和 2的两行，抽取多行时，行索引必须是列表的形式
# print(df.iloc[1])     # 根据索引号取行数据
# print(df.iloc[1,1])     # 根据索引号取单个值
# print(df.iloc[[1,4],:])     # 抽取第一行和第四行的数据
# print(df.iloc[1:4,:])     # 抽取第一行到第四行的数据
# print(df.iloc[:,0])# 抽取记录的第一列，但返回的是Series





chipo = read_csv('Pandas_exercises-master\chipotle.tsv', sep= '\t')
print(chipo)


# 查看前10行内容


# print(chipo[:10])
# head()方法就是从数据集开头预览，tail()是方法就是从数据集尾预览，不带参数默认显示头部的 5 条数据
# print(chipo.head(10))


# # 以一个元组（行数，列数）的形式返回数据框的形状
# print(chipo.shape)
#
# # 获取列数
# print(chipo.shape[1])
#
#
# # 返回对象的列索引
# columns返回一个index类型的列索引列表，data.columns.values返回的是列索引组成的ndarray类型
print(chipo.columns)
# print(chipo.columns.values)    # 通过columns字段获取，返回一个numpy型的array
# print(chipo.columns.values.tolist())   # df.columns 返回Index，可以通过 tolist(), 或者 list（array） 转换为list
# print(list(chipo))      # 直接使用 list 关键字，返回一个list


# # 获取行数
# print(chipo.shape[0])
# print(len(chipo))
# print(len(chipo.index))
#
#
# # 返回对象的行索引
# print(chipo._stat_axis.values.tolist())



# Index对象保存着索引标签数据，它可以快速找到标签对应的整数下标，其功能与Python的字典类似。
# index返回一个index类型的行索引列表，data.index.values返回的是行索引组成的ndarray类型
# print(chipo.index)
# print(chipo.index.values)


print(chipo[[ 'quantity', 'item_name']].groupby(by = 'quantity',as_index=False).max())
# print(chipo[['item_name','quantity']].groupby(by=['item_name']).sum().sort_values(by=['quantity'],ascending=False))