import pandas as pd
import numpy as np
from pandas import read_csv


'''''

salaries = pd.DataFrame({
    'name': ['BOSS', 'Lilei', 'Lilei', 'Han', 'BOSS', 'BOSS', 'Han', 'BOSS'],
    'Year': [2016, 2016, 2016, 2016, 2017, 2017, 2017, 2017],
    'Salary': [1, 2, 3, 4, 5, 6, 7, 8],
    'Bonus': [2, 2, 2, 2, 3, 4, 5, 6]
})


print(salaries)

print(salaries.sort_values('Salary',ascending=False))



'''''


'''''

dp = read_csv('Pandas_exercises-master/chipotle.tsv', sep='\t')
dp2 = dp[['quantity', 'item_name']]
# print(dp2)


# -- 查看前10行内容
# print(dp.head(10))

# -- 数据集中有多少个列(columns)？
# print(dp.shape[1])

# -- 打印出全部的列名称
# print(dp.columns.values.tolist())

# -- 数据集的索引是怎样的？
# print(dp.index)
# print(dp.index.values)

# -- 被下单数最多商品(item)是什么?

# sort_values()函数原理类似于SQL中的order by，可以将数据集依照某个字段中的数据进行排序，该函数即可根据指定列数据也可根据指定行的数据排序
# print(dp2.sort_values('quantity',ascending=False))   # by	指定列名(axis=0或'index')或索引值(axis=1或'columns')    ascending	是否按指定列的数组升序排列，默认为True，即升序排列
# print(dp2.groupby('item_name'))
# print(dp.groupby(dp['item_name']))

# DataFrame数据中的重复行，利用groupby累加合并
# print(dp2.groupby('item_name').sum())

# 对上面对数据根据item_name进行排序
# print(dp[['item_name','quantity']].groupby(by=['item_name']).sum().sort_values(by=['quantity'],ascending=False))


# -- 在item_name这一列中，一共有多少种商品被下单？

# 先把所有重复的商品合并，判断出销量大于0的商品
# dp3 = dp2.groupby('item_name').sum()
# print(dp3[dp3['quantity']>0].shape[0])

# 可直接统计dataframe中每列的不同值的个数,也可用于series,但不能用于list.返回的是不同值的个数.
# print(dp['item_name'].nunique())
# 统计list、series中的不同值的个数,返回的是list.
# print(np.unique(dp['item_name']))



# -- 在choice_description中，下单次数最多的商品是什么？
# print(dp[['choice_description','quantity']].groupby('choice_description').sum().sort_values('quantity',ascending=False))


# -- 一共有多少商品被下单？
# print(dp['quantity'].sum())

# -- 将item_price转换为浮点数

print(dp['item_price'])

dp['item_price']= dp['item_price'].apply(lambda x: float(x[1:]))
print(dp['item_price'])

# -- 在该数据集对应的时期内，收入(revenue)是多少？
# -- 在该数据集对应的时期内，一共有多少订单？
# -- 每一单(order)对应的平均总价是多少？



'''''









'''''


# 函数应用和映射,关于apply函数的格式为：apply(func,*args,**kwargs)的解释

df = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['utah', 'ohio', 'texas', 'oregon'])
print(df)


"""
               b         d         e
utah   -0.667969  1.974801  0.738890
ohio   -0.896774 -0.790914  0.474183
texas   0.043476  0.890176 -0.662676
oregon  0.701109 -2.238288 -0.154442
"""

# 将函数应用到由各列或行形成的一维数组上。DataFrame的apply方法可以实现此功能
f = lambda x: x+1
# 默认情况下会以列为单位，分别对列应用函数
t1 = df.apply(f)
print(t1)
# t2 = df.apply(f, axis=1)
# print(t2)

"""
b    1.597883
d    4.213089
e    1.401566
dtype: float64
utah      2.642770
ohio      1.370957
texas     1.552852
oregon    2.939397
dtype: float64
"""


# 除标量外，传递给apply的函数还可以返回由多个值组成的Series
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])


t3 = df.apply(f)
# 从运行的结果可以看出，按列调用的顺序，调用函数运行的结果在右边依次追加
print(t3)

"""
            b         d         e
min -0.896774 -2.238288 -0.662676
max  0.701109  1.974801  0.738890
"""

# 元素级的python函数，将函数应用到每一个元素
# 将DataFrame中的各个浮点值保留两位小数
f = lambda x: '%.2f' % x
t3 = df.applymap(f)
print(t3)
"""
            b      d      e
utah    -0.67   1.97   0.74
ohio    -0.90  -0.79   0.47
texas    0.04   0.89  -0.66
oregon   0.70  -2.24  -0.15
"""

# 注意，之所以这里用map,是因为Series有一个元素级函数的map方法。而dataframe只有applymap。
t4 = df['e'].map(f)
print(t4)

"""
utah     0.74
ohio     0.47
texas   -0.66
oregon  -0.15
"""
'''''