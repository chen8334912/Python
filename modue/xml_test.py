'''''

ElementTree生来就是为了处理XML，它在Python标准库中有两种实现：
一种是纯Python实现的，如xml.etree.ElementTree，
另一种是速度快一点的xml.etree.cElementTree。
注意：尽量使用C语言实现的那种，因为它速度更快，而且消耗的内存更少。

'''''


import xml.etree.ElementTree as ET

tree = ET.parse('xml_lesson')
root = tree.getroot()     # 获得root节点
# print(root.tag)
'''''
# 遍历xml文档

for child in root:
    print(child, child.tag, child.attrib)
    for i in child:
        print(i.tag)       # 当要获取节点名时，用tag方法。
        print(i.attrib)    # 当要获取属性值时，用attrib方法
        print(i.text)       # 当要获取节点值时，用text方法
        

# 只遍历year 节点

for node in root.iter('year'):
    print(node.tag,node.text)


# 修改

for i in root.iter('gdppc'):
    new_gdp = int(i.t)




for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")

tree.write("xmltest.xml")


# 删除

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')

'''''

'''''

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

try:
    tree = ET.parse("country.xml")  # 打开xml文档 
    # root = ET.fromstring(country_string) #从字符串传递xml 
    root = tree.getroot()  # 获得root节点  
except Exception, e:
    print
    "Error:cannot parse file:country.xml."
    sys.exit(1)
print
root.tag, "---", root.attrib
for child in root:
    print
    child.tag, "---", child.attrib

print
"*" * 10
print
root[0][1].text  # 通过下标访问 
print
root[0].tag, root[0].text
print
"*" * 10

for country in root.findall('country'):  # 找到root节点下的所有country节点 
    rank = country.find('rank').text  # 子节点下节点rank的值 
    name = country.get('name')  # 子节点下属性name的值 
    print
    name, rank

    # 修改xml文件 
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml') 



'''''