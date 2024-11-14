import re #1.字符串匹配主要是利用re模块

l =re.findall( r'\bf[a-z]*', 'which foot or hand fell fastest') #返回一个列表

print( l)
