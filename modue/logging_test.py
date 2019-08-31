import logging

'''''

可见在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，
可用参数有

stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout
或者文件(f=open('test.log','w'))，默认为sys.stderr。若同时列出了filename和
stream两个参数，则stream参数会被忽略



'''''

'''''
logging.basicConfig(    #  用默认日志格式（Formatter）为日志系统建立一个默认的流处理器（StreamHandler），设置基础配置（如日志级别等）并加到root logger（根Logger）中
    level=logging.DEBUG,   # level：设置rootlogger的日志级别
    filename='logger.log',    # filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
    filemode='w',    # filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
    format='%(asctime)s %(filename)s %(lineno)s %(message)s',  # format：指定handler使用的日志显示格式。
    datefmt='%a, %d %b %Y %H:%M:%S',    # datefmt：指定日期时间格式。
    # stream=''
)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息

'''''
'''''

handler名称：位置；作用

StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
FileHandler：logging.FileHandler；日志输出到文件
BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器


'''''

'''''

#---------logger对象

def logger():
    logger = logging.getLogger()    # 创建logger对象

    fh = logging.FileHandler('test.log')    # 创建一个handler，用于写入日志文件
    sh = logging.StreamHandler()      # 再创建一个handler，用于输出到控制台

    fm = logging.Formatter('%(asctime)s %(message)s %(name)s')   #  指定输出的格式和内容，format可以输出很多有用的信息

    fh.setFormatter(fm)    #  handler 通过 setFormatter() 方法设置此 Formatter 对象即可
    sh.setFormatter(fm)

    logger.addHandler(fh)    # Logger.addHandler() 和 Logger.removeHandler() 添加和删除一个Handler
    logger.addHandler(sh)

    logger.setLevel('DEBUG')    # 设置日志级别
    return logger


#  --------------将信息打印到控制台上

logger=logger()

logger.debug('logger debug message')
logging.info('logger info message')
logging.warning('logger warning message')
logging.error('logger error message')
logging.critical('logger critical message')


'''''

'''''



logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('rizhi.log')
format = logging.Formatter('%(asctime)s %(message)s %(name)s')
fh.setFormatter(format)
logger.addHandler(fh)




logger.debug('苍井空')
logger.info('麻生希')
logger.warning('小泽玛利亚')
logger.error('桃谷绘里香')
logger.critical('泷泽萝拉')


'''''

'''''

logger = logging.getLogger()
logger.setLevel('DEBUG')        # 设置根任务的日志级别


fh = logging.FileHandler('rizhi1.log')
sh = logging.StreamHandler()

sh.setLevel('INFO')     # 设置子任务的日志级别

format = logging.Formatter('%(asctime)s %(message)s %(name)s')

fh.setFormatter(format)
sh.setFormatter(format)

logger.addHandler(fh)
logger.addHandler(sh)



logger.debug('苍井空')
logger.info('麻生希')
logger.warning('小泽玛利亚')
logger.error('桃谷绘里香')
logger.critical('泷泽萝拉')


'''''

root3 = logging.getLogger()

logger1 = logging.getLogger('chris')
logger1.setLevel('DEBUG')  # 设置根任务的日志级别

logger2 = logging.getLogger('fish')
logger2.setLevel('INFO')

fh = logging.FileHandler('rizhi2.log')
sh = logging.StreamHandler()

format = logging.Formatter('%(asctime)s--%(levelname)s--%(message)s--%(name)s')

fh.setFormatter(format)
sh.setFormatter(format)

logger1.addHandler(fh)
logger1.addHandler(sh)

logger2.addHandler(fh)
logger2.addHandler(sh)

# root3.addHandler(fh)
# root3.addHandler(sh)


# root3.debug('苍')
# root3.info('麻')
# root3.warning('小泽玛')
# root3.error('桃谷绘')
# root3.critical('泷泽')


logger1.debug('苍井空')
logger1.info('麻生希')
logger1.warning('小泽玛利亚')
logger1.error('桃谷绘里香')
logger1.critical('泷泽萝拉')

logger2.debug('苍井')
logger2.info('麻生')
logger2.warning('小泽玛利')
logger2.error('桃谷绘里')
logger2.critical('泷泽萝')

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'logger.log',
    filemode = 'w',
    format = '%(filename)s %(asctime)s [%(lineno)s] %(message)s',
    # datefmt = ''
)



logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')