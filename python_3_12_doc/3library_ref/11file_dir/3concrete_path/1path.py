from pathlib import *

#1.具体路径是纯路径的子类

#2.三种实例化的办法
#2.1 class pathlib.Path( *pathsegments)
print( Path('setup.py'))

#2.2 class pathlib.PosixPath( *segments)

#2.3 class pathlib.WindowsPath( *segments)

#3.只能实例化和当前操作系统一致的类，否则将报错
import os
print( os.name)#posix
WindowsPath('setup.py')#会报错
