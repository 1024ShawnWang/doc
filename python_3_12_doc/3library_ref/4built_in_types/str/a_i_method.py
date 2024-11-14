
print( str.capitalize( 'wang xu') )#1.首字母大写

print( str.casefold('wAng XU'))#2.全部小写

print( 'wang'.center( 7, )  )#3.把'wang'放在长度为7的字符串中间，默认的填充符号是空格

print( 'wangxu'.count('gx') )#子字符串出现次数，可以切片

print( 'wangxu'.encode( encoding='utf-8') )#5.返回bytes对象，根据指定解码方式

print( 'wangxu'.endswith('xu') )#6.字符串是否按指定字符串结尾，支持切片操作

print( 'wang\txu'.expandtabs() )#7.将\t转为制表符，默认制表符的每个项目的开头分别在0， 8， 16， 依次递推，这就是为什么叫制表符的原因了😅

print( 'wangxu'.find('g') )#8.返回子字符串的最小索引，支持切片操作，搜索不到返回-1

print( 'wangxu has {0}'.format(1+2) )#9.支持数字占位符

#10. str.format_map( mapping)

print( 'wangxu'.index('g') )#11.约等于find，但是这个找不到给定值会报错，ValueError

print( 'wangxu1'.isalnum() )#12.字符串是否全数字和字母组成并且非空，如果是，返回true

print( 'wangxu'.isalpha() )#13.字符串非空，并且所有字符是字母

print( '¥abc'.isascii() )#14.字符串是否全是ascill字符，utf-8编码下的范围是    0000-007F

print( '123'.isdecimal() )#15.检测是否是十进制字符

print( '123w'.isdigit() ) #16.检测是否全是数字

#17 str.isidentifier()

print( 'wangxu'.islower() ) #18.字符串非空，并且全是小写返回True，否则False
print( ''.islower() )

print( ''.isnumeric() ) #19.非空，并且全是数值类型的，返回True，数值类型的定义要参考Unicode，只要一个字符可以转为unicode的数字值，可能就是数值类型
#注意isdigit()方法比较

print( ''.isprintable() ) #20.字符串为空，或者所有字符可打印就返回True，不可打印的字符在unicode中被定义为 Other，或者 Seperator的字符

print( '    '.isspace() ) #21.非空，并且只有空白字符就返回True， 否则False，空白字符包括，空格，制表，。。。

print( 'Wang Xu'.istitle() )  #22.非空，并且所有单词首字母大写（title的格式），返回True，否则False

print( 'WANG XU'.isupper() )  #23.非空，全部大写返回True，否则False，对比islower() 
