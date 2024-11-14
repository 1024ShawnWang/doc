
l=['wang', 'xu']
print( ' '.join( l)) #24.用空格拼接指定的可迭代对象，注意拼接只在内部进行

print( 'wangxu'.ljust( 8, 'a')) #25.类比center()办法，将字符串放在左边达不到指定长度，就用'a'凑

print( 'WangXu'.lower() )  #26.将字符全都换成小写

print( 'www.wangxu.com'.lstrip('w.')) #27.移除左边的全部的给定参数的组合，默认参数是空白字符，这个的结果是angxu.com

#28. static str.maketrans()

print( 'wangxu'.partition('g') ) #29如果发现分隔符，，返回一个三元元组，('wan', 'g', 'xu')，没有的话，后面两个都是空

print( 'wangxu'.removeprefix( 'wang') ) #30.移除指定前缀，对比和lstrip的不同，这里面没有组合，机械地移除

print( 'wangxu'.replace('gx', 'kk', 1) ) #31.替换，并且可以指定替换发生的次数，默认是所有

print( 'wangxug'.rfind('g') )  #32.找到给定字符串最大索引（最右）索引，否则返回-1

print( 'wangxug'.rindex('g') )  #33.同rfind一样，只不过找不到的时候会报错ValueError，回忆find与index的关系，一样的

#34. str.rjust() 右对齐，对比 str.ljust() 办法

#35. str.rpartition( sep)  对比 str.partition( sep)办法，不同的是，这里是最后一次出现的位置进行划分

#36. str.rsplit( sep) 从右边开始划分， 没有 str.lsplit ，但是有即将出现的 str.split

print( '1$2$$3'.rsplit( '$') )  #37.按指定字符串分割给定的字符，对于单个字符，rsplit和split没有什么区别

#38. str.rstrip() 对比  str.lstrip()

print(  '1,2,3,'.split(',') ) #39. 分割

print( 'ab\nc\rd'.splitlines() ) #40.按行边界进行分割，行边界的定义有如下字符\n \r .... 

#41.str.startswith('prefix') 对比 endswith


#42. str.strip 移除字符串里面所有组合


print( 'Wang Xu'.swapcase() )#43.大小写颠倒

print( 'wang xu'.title() ) #44.做成title格式，（也就是每个元素，首字母大写，其他小写）

print( 'wangxu'.upper() )  #45.全部变成大写，对比str.lower()

print( 'wangxu'.zfill(9) )  #46.不足长度填充0，有正负号的在正负号之后填充。给定的宽度小于长度时候不变，类比各种填充办法，比如str.center
#或者 str.ljust  str.rjust，流程类似
