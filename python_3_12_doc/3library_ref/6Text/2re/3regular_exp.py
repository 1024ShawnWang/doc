#正则表达式对象
#class re.Pattern

import re

reg =re.compile( r'\W')
print( type(reg)) #1.由re.compile(pattern) 返回一个re.Pattern对象
#有什么类似的对象生成吗?  l=list()
#l =list(1,2,3) #错误，list只能接受一个参数
l=list( (1,2,3)) #传入一个tuple
print( l)

#2.Pattern.search( string[, pos[, endpos]] ) 第一个位置

#3.Pattern.match #默认只能从最开头开始

#4.Pattern.fullmatch #整个字符

#5.相同点，这三个函数的参数都一样;不同点，search指定段的某个子串就行，match，子串开头就要开始匹配，fullmatch指定子串全体

#6.Pattern.split( string, maxsplit=0) == split()函数，返回列表

#7.Pattern.findall( string[, pos[, endpos]] ) 返回一个列表，非重叠的

#8.Pattern.finditer

#9.Pattern.sub

#10.Pattern.subn

#11.Pattern.flags

#12.Pattern.groups

#13.Pattern.groupindex

print( reg.pattern) #14.Pattern.pattern
