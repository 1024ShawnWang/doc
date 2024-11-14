
#1. re.compile( pattern, flags=0) 将正则表达式的样式编译为一个 正则表达式对象
# flags的值，可以是 flags.py中 flags中的任意值。

#2. re.search( pattern, string, flags=0) 从左到右匹配第一个字符串，返回Match对象，如果没有，返回None

#3. re.match( pattern, string, flags=0) 从第一个字符开始匹配，匹配成功返回Match对象，否则None

#4. re.fullmatch( p, s, flags=0) 整个字符串

#5. re.split( pattern, string, maxsplit=0, flags=0) 用pattern分开string。

#6. re.findall( pattern, string, flags=0) 返回pattern在sting中所有的非重叠匹配列表

#7. re.finditer( pattern, string, flags=0) 对比6，这里返回一个match对象的迭代器

#8. re.sub( pattern, repl, string, count=0, flags=0) 用repl替换string最左边的非重叠出现的pattern 来获得字符串，返回一个字符串

#9. re.subn(p, r, s, count=0, flags=0) 对比8，不同是返回一个元组( 字符串，替换次数）

#10. re.escape( pat) 转义pattern中的特殊字符

#11. re.purge() 清除正则表达式的缓存


