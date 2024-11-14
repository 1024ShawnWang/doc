
#给异常增加说明笔记

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('做了一写说明笔记')  #1.使用 add_note()方法
    e.add_note('再做一些说明')
    raise

#3.12有
