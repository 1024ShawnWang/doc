
#下面所写的默认都是pdb模式下
# 程序在运行完断点后停下，一般也就是断点的下一句开始的时候停下来。

#1.pdb模式下，输出空白行（什么都不做，直接回车)将会重复最后一条命令

#2.!开头的命令，将会作为python语句，直接在当前环境下执行

#3.h(elp)

#4.w(here) 打印栈回溯？

#5.d(own) 在栈中，向下1级。  尚未执行的语句？


#6.u(p)   对比5


#7.b(reak)


#8.tbreak

#9.cl(ear)

#10.disable 禁用断点


#11.enable xxx  

#12.ignore

#13.condition   条件为真大时候，启动断点

#14.commands

#15.s(tep)  运行当前行，之后在第一个可以停下的位置停下

#16.n(ext) next 直到运行到当前函数下一行停止

#17.unt(il) [lineno]运行到指定行号

#18.r(eturn)  继续运行，直到当前函数返回

#19.c(ont(inue))  继续运行，直到碰到下一断点

#20.j(ump) [lineno] 对比 until

#21.l(ist) 列出源代码，当前帧的当前行用-->表示

#22.ll (long list)

#23.a(rgs)打印当前函数的参数，和参数目前的值

#24.p(rint) [expression] 在当前上下文求解expression对值，并且打印

#25.pp

#26.wahtis expression
