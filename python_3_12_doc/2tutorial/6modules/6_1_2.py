
#模块被引入时候，搜索优先级和路径
#1. 内置模块 (sys.builtin_module_names)
#2. 在 sys.path()路径内搜索 指定模块.py 的文件
import sys
print( sys.path )

#3. sys.path的值依赖于三个方面.... 不记了，自己看文档

#4.可以看到sys.path和 ubuntu系统中的 $PATH

#5. sys.path会包含 运行脚本的目录在第一位， 所以自己写的模块，会比标准库调用的更快

#6. 

