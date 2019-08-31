
import configparser

'''''

#------创建文档

config = configparser.ConfigParser()        # config = {}
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['sdaf.sdjklf'] = {}
config['sdaf.sdjklf']['Name'] = 'Chris'


config["sdafsad"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here


with open('example.ini', 'w') as configfile:
    config.write(configfile)




#------读取文档



config = configparser.ConfigParser()

config.read('example.ini')

print(config.sections())    # 打印节

print('bytebong.com' in config, 'DEFAULT' in config, 'name' in config)

print(config['sdaf.sdjklf']['name'])    # 不区分大小写

for key in config['bitbucket.org']:
    print(key)       # 遍历任何字典，都会把 DEFAULT(系统默认) 字典内容遍历出来

print(config.options(
    'bitbucket.org'))    #  ['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']

print(config.items(
    'bitbucket.org'))

print(config.get('bitbucket.org','compressionlevel'))

'''''


#------操作文档

config = configparser.ConfigParser()

config.read('example.ini')

# config.add_section('micheal')     # 添加节
# config.set('micheal','sex','boy')     # 添加节下面的键值对


# config.remove_section('micheal')     # 删除节
config.remove_option('micheal','age')     # 删除节下面的键值对

config.write(open('i.cfg','w'))