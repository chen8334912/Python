import os

# print(os.path.split('/Volumes/Work/Python/web/web1/web2/cal.py'))
# print(os.path.dirname('/Volumes/Work/Python/web/web1/web2/cal.py'))
# print(os.path.basename('/Volumes/Work/Python/web/web1/web2/cal.py'))
# print(os.path.isabs('/Volumes/Work/Python/web/web1/web2/cal.py'))
# print(os.path.isabs('/Volumes/Work/Python/web/web1/web2'))      #  如果path是绝对路径，返回True
# print(os.path.isfile('/Volumes/Work/Python/web/web1/web2/cal.py'))      #  如果path是一个存在的文件，返回True。否则返回False
# print(os.path.isdir('/Volumes/Work/Python/web/web1/web2/cal.py'))      #  如果path是一个存在的目录，则返回True。否则返回False


a = '/Volumes/Work/Python/web'
b = 'web1/web2/cal.py'
c = os.path.join(a, b)
print(os.path.isabs(c))

print(os.path.getatime('/Volumes/Work/Python/web/web1/web2/cal.py'))      #  返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime('/Volumes/Work/Python/web/web1/web2/cal.py'))      #  返回path所指向的文件或者目录的最后修改时间
