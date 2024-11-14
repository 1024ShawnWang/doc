

'''open( filename, mode='r', encoding=None)，更多参数请看文档

mode有七种，如下
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of file if it exists
'b' binary mode
't' text mode (default)
'+' open for updating (reading and writing)

当选择b的时候，读写二进制文件，是不可以指定编码方式的（这很显然）

encoding 默认参数是依赖平台的
'''

#2.推荐使用with来更简短的操作文件对象
