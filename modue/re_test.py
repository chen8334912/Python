'''''

元字符：. ^ $ * + ? { } [ ] | ( ) \

'''''

import re

# 元字符：. ^ $ * + ? { } [ ] | ( )

# ret = re.findall('a...vi...','hellosafsdafalvijhkhk')  # 一个.代表一个字符
# ret = re.findall('\d+','fsaf22dsfmdsf888jj37')
# ret = re.findall('^a...vi...','hellosafsdafalvijhkhk')   # ^代表在字符串的开头匹配
# ret = re.findall('a...n$', 'alvinhelloawwwnccc')   # $代表在字符串的结尾匹配
# ret = re.findall('abc*', 'abccccffZZZ999')  # 贪婪匹配 [0,+oo]
# ret = re.findall('alex*', 'acccbccale')  # 贪婪匹配 [0,+oo]
# ret = re.findall('(abc)*', 'abccccffZZZ999')  # 贪婪匹配 [0,+oo]
# ret = re.findall('alex+', 'accalexxxxxx')  # 贪婪匹配 [1,+oo]
# ret = re.findall('alex?','akjflafjalexxxx')  # 贪婪匹配 [0,1]
# ret = re.findall('abc{1,}', 'abcccdsa')  # {0,}==* , {1,}==+, {0,1}==?, {6}==6, {1,6}==1-6
# ret=re.findall('abc*?','abcccccc')   # 惰性匹配，按照最小的匹配

'''''


# 在字符集里有功能的符号: - 什么到什么     ^ 非，匹配除什么之外       \ 转义符，反斜杠后边跟元字符去除特殊功能

\d   匹配任何十进制数；它相当于类 [0-9]。
\D   匹配任何非数字字符；它相当于类 [^0-9]。
\s   匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
\S   匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
\w   匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
\W   匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
\b   匹配一个特殊字符边界，比如空格 ，&，＃等

'''''

# --------------------------------------------字符集[]

# ret = re.findall('a[c d]d','abcda dacd')            # findall返回所有满足匹配条件的结果,放在列表里
# ret = re.findall('q[a-z]','qcb')
# ret = re.findall('q[a-z]*','qcbsdfdsf089jlksjalf')
# ret = re.findall('\([^()]\)','12+(23*56+2-5*(2-1))')
# ret = re.findall('www\.baidu','www.baidu')
# ret = re.findall(r'I\b','hello I am LIST')        # r表示在python层级不做任何转义，直接在re模块里转义
# ret = re.findall(r'kssa|b','sfksadkssalbkssaf')        # |表示或者
# ret = re.findall('(?P<id>\d{2})/(?P<name>\w{3})','23/com')            # ?P<>表示分组
# ret = re.findall('(?P<id>[a-z]+)\d+','alex123xlkjlk123jklj324')

# re.match('a','abc').group()     # 同search,不过尽在字符串开始处进行匹配
# ret = re.search('(?P<name>[a-z]+)(?P<age>\d+)','alex123xlkjlk123jklj324').group('age')            # 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以

# ret = re.split(' ','hello world')
# ret = re.split('[ |]','hello worl|d')
# ret = re.split('[ab]','abcd')     # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割

# ret=re.sub('\d','abc','alvin555yuan6',1)     # 替换
# ret = re.subn('\d','abc','alvin555yuan6')    # 替换后的结果和替换的次数

obj=re.compile('\d{3}')
ret=obj.search('abc123eeee')
print(ret.group())


# print(ret)



'''''


# --------------------------------------------字符集[]
ret = re.findall('a[bc]d', 'acd')
print(ret)  # ['acd']

ret = re.findall('[a-z]', 'acd')
print(ret)  # ['a', 'c', 'd']

ret = re.findall('[.*+]', 'a.cd+')
print(ret)  # ['.', '+']

# 在字符集里有功能的符号: - ^ \

ret = re.findall('[1-9]', '45dha3')
print(ret)  # ['4', '5', '3']

ret = re.findall('[^ab]', '45bdha3')
print(ret)  # ['4', '5', 'd', 'h', '3']

ret = re.findall('[\d]', '45bdha3')
print(ret)  # ['4', '5', '3']


'''''