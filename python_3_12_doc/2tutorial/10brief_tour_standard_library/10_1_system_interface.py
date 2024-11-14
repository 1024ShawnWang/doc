
import os

print( os.getcwd() )   #1.get current working directory 得到目前运行文件所在的目录

print( os.chdir('/etc'))  #2.change directory to /etc 返回值是None
print( os.getcwd() )#再次获得系统当前工作目录验证上面命令的正确执行

os.system('echo "Hello"') #3.在系统shl中执行 echo "Hello"

#4. 使用 import os ，而不是 from os import *，因为os.open()和内置的函数open()的用法非常不一样

print( dir( os))  #5.内置函数dir ,可以列出****os模块*****的所有文件

#help( os)  #6.内置函数help，可以提供这个模块的手册

#7. shutil模块提供了更好的接口对于日常的文件 管理
