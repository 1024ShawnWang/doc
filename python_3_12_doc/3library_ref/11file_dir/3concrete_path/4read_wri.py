from pathlib import *

#1. Path.open(mode='r', buffering-1, encoding=None, errors=None, newline=None) #打开指定路径的文件，就像内置open函数一样，但是这里需要Path对象
p=Path('test.txt')
with p.open() as f:
    print( f.readline() )  #注意python读取一行也会读取换行符，所以打印出来的话，是两行，一行文本，一行空白

#2. read_text( encoding=None, errors=None)

#3. read_bytes()

#4. write_text( data, encodign=None,  errors=None, newline=None)

#5. write_bytes( data)
