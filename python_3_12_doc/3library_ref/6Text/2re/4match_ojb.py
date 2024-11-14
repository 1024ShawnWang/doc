import re
#1.class re.Match对象布尔值总为 True, search和match方法使用成功就会返回一个match对象

#2.Match.expand( template)

#3.Match.group( [group1, ...]) 一个参数就返回一个字符串，多个参数返回一个元组
m= re.match( r"(\w+) (\w+)", "Isaac Newton, physicist") #注意是 w 还是W, w for word
print( m.group( 0)) #匹配的全部
print( m.group( 1))
print( m.group( 1, 2))

#3.1 group也可以变成一个字典 且 列表
ma = re.match( r'(?P<first_name>\w+) (?P<last_name>\w+)', 'malcolm reynolds')
print( ma.group('first_name'))
print( ma.group(1))#两者是一致的，注意group(0)是全体

#3.2 如果一个组匹配成功多次，只会返回最后一个匹配
mat =re.match( r'(..)+', 'a1b2c3')
print( mat.group(1)) #？可是match不是必须从开头开始匹配吗
#可能成功匹配成功多次就是 + ?等操作符

#3.3 Match.__getitem__(g) == m.group( g)

print( mat.groups() )#对比mat.group( 1)  Match.groups( default=None)

#4. Match.groupdict( default=None)

#5. Match.start( [group])

#6. Match.end( [group])
email = 'tony@tiremove_thisger.net'
matc = re.search(r'remove_this', email)
l =email[:matc.start()] + email[matc.end():] #6.1 end 和 start()会返回索引
print( l)

#7. Match.span( [group])

#8. Match.pos

#9. Match.endpos

#10.Match.lastindex

#11.Match.lastgroup

#12.Match.re

#13. Match.string
