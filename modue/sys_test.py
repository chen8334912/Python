import sys

# print(sys.version)
print(sys.argv)



'''''
进度条


import sys, time
for i in range(10):
    sys.stdout.write('*')
    time.sleep(0.1)
    sys.stdout.flush()      # flush 刷新缓存


'''''