
#1. dict.keys();  dict.values();  dict.itesm() 返回的都是字典视图对象
l={x:x**2 for x in range(4) }
print( l)
print( l.values())


#2.len

#3.iter


#4. in

#5. reversed( dictview)

#6. dictview.mapping 

#7. hashable 一：生命周期不改变hash值（python解释器分配的） 二：可比较
#简单地说 实现了两个魔术方法 __hash__()  __eq__()

