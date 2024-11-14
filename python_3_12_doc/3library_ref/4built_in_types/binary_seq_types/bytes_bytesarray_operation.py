
 #1.两个对象都支持通用序列操作    in, not, *, 索引，切片， 长度， max， min, index, count
a=b'abc'
b=a.replace(b'a', b'f')
print( b)

#2.bytesarray作为可变对象，支持可变序列的通用操作：包括 s[i]=x(替换), s[i:j]=t(替换),   del,  append, clear, copy, extend, s *= n, insert, pop, remove, reverse

#3.两个对象基本都可以像str那些操作，我当然可以逐个的学习，但是作为一个字典，既然已经知道解决了什么问题，也许问题真正出现的时候再学习吧

#eg 
c =b'wangxu'
d = c.removesuffix( b'gxu')
print( d)
