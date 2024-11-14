
#1. 线程本地数据 是 特定线程的数据。管理线程本地数据，只需要创建 一个 local的 实例，并在实例中存储属性
'''
mydata = threading.local()
mydata.x = 1
'''

#2. class threading.local 一个代表线程本地数据的类


