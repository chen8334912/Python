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

# 探索Chipotle快餐数据


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

# print(dp['item_price'])
# dp['item_price']= dp['item_price'].apply(lambda x: float(x[1:]))
# print(dp['item_price'])

# -- 在该数据集对应的时期内，收入(revenue)是多少？

# print(dp[['item_price','quantity']])
# print((dp['quantity'] * dp['item_price']).sum())



# -- 在该数据集对应的时期内，一共有多少订单？
# print(dp['order_id'].nunique())




# -- 每一单(order)对应的平均总价是多少？















# 探索2012欧洲杯数据
# -- 将数据集命名为euro12
euro12 = read_csv('Pandas_exercises-master/Euro2012.csv')
print(euro12)

# -- 只选取Goals这一列
print(euro12['Goals'])

# -- 有多少球队参与了2012欧洲杯？
print(euro12['Team'].nunique())

# -- 该数据集中一共有多少列(columns)?

print(euro12.columns.values.tolist())
print(euro12.shape[1])

# -- 将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框


'''''







-- 对数据框discipline按照先Red
Cards再Yellow
Cards进行排序
-- 计算每个球队拿到的黄牌数的平均值
-- 找到进球数Goals超过6的球队数据
-- 选取以字母G开头的球队数据
-- 选取前7列
-- 选取除了最后3列之外的全部列
-- 找到英格兰(England)、意大利(Italy)
和俄罗斯(Russia)
的射正率(Shooting
Accuracy)

import pandas as pd

# 将数据集命名为euro12
euro12 = pd.read_csv('C:\\Users\\Administrator\\Desktop\\Euro2012.csv')

# 只选取 Goals 这一列
euro12.Goals

# 有多少球队参与了2012欧洲杯？
euro12.Team.nunique()

# 该数据集中一共有多少列(columns)?
euro12.shape[1]

# 将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# 对数据框discipline按照先Red Cards再Yellow Cards进行排序
discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)

# 计算拿到的黄牌数的平均值
euro12['Yellow Cards'].mean()

# 找到进球数Goals超过6的球队数据
euro12[euro12.Goals > 6]

# 选取以字母G开头的球队数据
euro12[euro12.Team.str.startswith('G')]

# 选取前7列
euro12.iloc[:, 0:7]

# 选取除了最后3列之外的全部列
euro12.iloc[:, 0:-3]

# 找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]

# loc：通过行标签索引数据
# iloc：通过行号索引行数据
# ix：通过行标签或行号索引数据（基于loc和iloc的混合）


练习3 - 数据分组
探索酒类消费数据
-- 将数据框命名为drinks
-- 哪个大陆(continent)
平均消耗的啤酒(beer)
更多？
-- 打印出每个大陆(continent)
的红酒消耗(wine_servings)
的描述性统计值
-- 打印出每个大陆每种酒类别的消耗平均值
-- 打印出每个大陆每种酒类别的消耗中位数
-- 打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值

import pandas as pd

# 将数据框命名为drinks
drinks = pd.read_csv('C:\\Users\\Administrator\\Desktop\\drinks.csv')

# 哪个大陆(continent)平均消耗的啤酒(beer)更多？
(drinks[['continent', 'beer_servings']].groupby(by=['continent']).mean().sort_values(by=['beer_servings'],
                                                                                     ascending=False)).head(1)

# 打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
drinks.groupby('continent').wine_servings.describe()

# 打印出每个大陆每种酒类别的消耗平均值
drinks.groupby('continent').mean()

# 打印出每个大陆每种酒类别的消耗中位数
drinks.groupby('continent').median()

# 打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
drinks.groupby('continent').spirit_servings.describe()

练习4 - Apply函数
探索1960 - 2014
美国犯罪数据
-- 将数据框命名为crime
-- 每一列(column)
的数据类型是什么样的？
-- 将Year的数据类型转换为
datetime64
-- 将列Year设置为数据框的索引
-- 删除名为Total的列
-- 按照Year（每十年）对数据框进行分组并求和
-- 何时是美国历史上生存最危险的年代？



import pandas as pd

# 将数据框命名为drinks
crime = pd.read_csv('C:\\Users\\Administrator\\Desktop\\US_Crime_Rates_1960_2014.csv', index_col=0)

# 每一列(column)的数据类型是什么样的？
crime.info()

# 将Year的数据类型转换为 datetime64
crime.Year = pd.to_datetime(crime.Year, format='%Y')

# 将列Year设置为数据框的索引
crime = crime.set_index('Year', drop=True)

# 删除名为Total的列
del crime['Total']
crime.head()

# 按照Year（每十年）对数据框进行分组并求和
crimes = crime.resample('10AS').sum()
population = crime.resample('10AS').max()  # 人口是累计数，不能直接求和
crimes['Population'] = population

# 何时是美国历史上生存最危险的年代？
crime.idxmax(0)  # 最大值的索引值

练习5 - 合并¶
探索虚拟姓名数据
-- 创建DataFrame
-- 将上述的DataFrame分别命名为data1, data2, data3
-- 将data1和data2两个数据框按照行的维度进行合并，命名为all_data
-- 将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col
-- 打印data3
-- 按照subject_id的值对all_data和data3作合并
-- 对data1和data2按照subject_id作连接
-- 找到
data1
和
data2
合并之后的所有匹配结果

import pandas as pd
import numpy as np

raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
# 创建DataFrame
# 将上述的DataFrame分别命名为data1, data2, data3
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

# 将data1和data2两个数据框按照行的维度进行合并，命名为all_data
all_data = pd.concat([data1, data2], axis=0)

# 将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col
all_data_col = pd.concat([data1, data2], axis=1)

# 打印data3
data3

# 按照subject_id的值对all_data和data3作合并
pd.merge(all_data, data3, on='subject_id')

# 对data1和data2按照subject_id作内连接
pd.merge(data1, data2, on='subject_id', how='inner')

# 找到 data1 和 data2 合并之后的所有匹配结果
pd.merge(data1, data2, on='subject_id', how='outer')

练习6 - 统计
探索风速数据
-- 将数据作存储并且设置前三列为合适的索引
-- 2061
年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug
-- 将日期设为索引，注意数据类型，应该是datetime64[ns]
-- 对应每一个location，一共有多少数据值缺失
-- 对应每一个location，一共有多少完整的数据值
-- 对于全体数据，计算风速的平均值
-- 创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差
-- 创建一个名为day_stats的数据框去计算并存储所有location的风速最小值，最大值，平均值和标准差
-- 对于每一个location，计算一月份的平均风速
-- 对于数据记录按照年为频率取样
-- 对于数据记录按照月为频率取样

import pandas as pd
import datetime

# 将数据作存储并且设置前三列为合适的索引
df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\wind.data', sep='\s+', parse_dates=[[0, 1, 2]])


# 2061年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug
def fix_century(x):
    year = x.year - 100 if x.year > 1999 else x.year
    return datetime.date(year, x.month, x.day)


df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_century)

# 将日期设为索引，注意数据类型，应该是datetime64[ns]
df['Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy'])
df = df.set_index('Yr_Mo_Dy')

# 对应每一个location，一共有多少数据值缺失
df.isnull().sum()

# 对应每一个location，一共有多少完整的数据值
df.shape[1] - df.isnull().sum()

# 对于全体数据，计算风速的平均值
df.mean().mean()

# 创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差
loc_stats = pd.DataFrame()
loc_stats['min'] = df.min()
loc_stats['max'] = df.max()
loc_stats['mean'] = df.mean()
loc_stats['std'] = df.std()

# 创建一个名为day_stats的数据框去计算并存储所有天的风速最小值，最大值，平均值和标准差
day_stats = pd.DataFrame()
day_stats['min'] = df.min(axis=1)
day_stats['max'] = df.max(axis=1)
day_stats['mean'] = df.mean(axis=1)
day_stats['std'] = df.std(axis=1)

# 对于每一个location，计算一月份的平均风速
df['date'] = df.index

df['year'] = df['date'].apply(lambda df: df.year)
df['month'] = df['date'].apply(lambda df: df.month)
df['day'] = df['date'].apply(lambda df: df.day)

january_winds = df.query('month ==1')  # query等同于df[df.month==1]
january_winds.loc[:, 'RPT':'MAL'].mean()

# 对于数据记录按照年为频率取样
df.query('month ==1 and day == 1')

# 对于数据记录按照月为频率取样
df.query('day == 1')

练习7 - 可视化
探索泰坦尼克灾难数据
-- 将数据框命名为titanic
-- 将PassengerId设置为索引
-- 绘制一个展示男女乘客比例的扇形图
-- 绘制一个展示船票Fare, 与乘客年龄和性别的散点图
-- 有多少人生还？
-- 绘制一个展示船票价格的直方图

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 将数据框命名为titanic
titanic = pd.read_csv('C:\\Users\\Administrator\\Desktop\\train.csv')

# 将PassengerId设置为索引
titanic = titanic.set_index('PassengerId')

# 绘制一个展示男女乘客比例的扇形图
Male = (titanic.Sex == 'male').sum()
Female = (titanic.Sex == 'female').sum()

proportions = [Male, Female]

plt.pie(proportions, labels=['Male', 'Female'], shadow=True,
        autopct='%1.1f%%', startangle=90, explode=(0.15, 0))
plt.axis('equal')
plt.title('Sex Proportion')
plt.tight_layout()
plt.show()

# 绘制一个展示船票Fare, 与乘客年龄和性别的散点图
lm = sns.lmplot(x='Age', y='Fare', data=titanic, hue='Sex', fit_reg=False)
lm.set(title='Fare x Age')

# 设置坐标轴取值范围
axes = lm.axes
axes[0, 0].set_ylim(-5, )
axes[0, 0].set_xlim(-5, 85)

# 有多少人生还？
titanic.Survived.sum()

# 绘制一个展示船票价格的直方图
df = titanic.Fare.sort_values(ascending=False)

plt.hist(df, bins=(np.arange(0, 600, 10)))
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')
plt.show()

练习8 - 创建数据框
探索Pokemon数据

-- 创建一个数据字典
-- 将数据字典存为一个名叫pokemon的数据框中
-- 数据框的列排序是字母顺序，请重新修改为name, type, hp, evolution, pokedex这个顺序
-- 添加一个列place['park', 'street', 'lake', 'forest']
-- 查看每个列的数据类型

import pandas as pd

# 创建一个数据字典
raw_data = {"name": ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
            "evolution": ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no', 'yes', 'no']
            }
# 将数据字典存为一个名叫pokemon的数据框中
pokemon = pd.DataFrame(raw_data)

# 数据框的列排序是字母顺序，请重新修改为name, type, hp, evolution, pokedex这个顺序
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]

# 添加一个列place['park','street','lake','forest']
pokemon['place'] = ['park', 'street', 'lake', 'forest']

# 看每个列的数据类型
pokemon.dtypes

练习9 - 时间序列
探索Apple公司股价数据
-- 读取数据并存为一个名叫apple的数据框
-- 查看每一列的数据类型
-- 将Date这个列转换为datetime类型
-- 将Date设置为索引
-- 有重复的日期吗？
-- 将index设置为升序
-- 找到每个月的最后一个交易日(business
day)
-- 数据集中最早的日期和最晚的日期相差多少天？
-- 在数据中一共有多少个月？
-- 按照时间顺序可视化Adj
Close值

import pandas as pd

# 读取数据并存为一个名叫apple的数据框
apple = pd.read_csv('C:\\Users\\Administrator\\Desktop\\appl_1980_2014.csv')

# 查看每一列的数据类型
apple.dtypes

# 将Date这个列转换为datetime类型
apple.Date = pd.to_datetime(apple.Date)

# 将Date设置为索引
apple = apple.set_index('Date')

# 有重复的日期吗？
apple.index.is_unique

# 将index设置为升序
apple = apple.sort_index(ascending=True)

# 找到每个月的最后一个交易日(business day)
apple_month = apple.resample('BM').mean()
apple_month.head()

# 数据集中最早的日期和最晚的日期相差多少天？
(apple.index.max() - apple.index.min()).days

# 在数据中一共有多少个月？
len(apple_month)

# 按照时间顺序可视化Adj Close值
apple['Adj Close'].plot(title='Apple Stock').get_figure().set_size_inches(9, 5)

练习10 - 删除数据
探索Iris纸鸢花数据
-- 将数据集存成变量iris
-- 创建数据框的列名称['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
-- 数据框中有缺失值吗？
-- 将列petal_length的第10到19行设置为缺失值
-- 将petal_lengt缺失值全部替换为1
.0
-- 删除列class
-- 将数据框前三行设置为缺失值
-- 删除有缺失值的行
-- 重新设置索引

import pandas as pd
import numpy as np

# 读取数据并存为一个名叫apple的数据框
iris = pd.read_csv('C:\\Users\\Administrator\\Desktop\\iris.data')

# 创建数据框的列名称['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class']
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# 数据框中有缺失值吗？
iris.isnull().sum()

# 将列petal_length的第10到19行设置为缺失值
iris['petal_length'].loc[10:19] = np.nan

# 将petal_lengt缺失值全部替换为1.0
iris.petal_length.fillna(1, inplace=True)

# 删除列class
del iris['class']

# 将数据框前三行设置为缺失值
iris.loc[0:2, :] = np.nan

# 删除有缺失值的行
iris = iris.dropna(how='any')

# 重新设置索引
iris = iris.reset_index(drop=True)  # 加上drop参数，原有索引就不会成为新的列


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


