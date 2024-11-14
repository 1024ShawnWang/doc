

with open('test.txt') as f: # 默认为读，默认解码就是uft-8
    print( f.read())    #1. 默认将读取全部文件到内存，如果内存比文件小就完蛋了，可选参


#2.readlines
# 3.12之后可以直接 for line in f了，而不用readlines()

#3.write

#4.seek

#5.import json

#6.基本没看懂思密达，但是重要的是知道自己不知道，到时候记得查官方文档就好了
