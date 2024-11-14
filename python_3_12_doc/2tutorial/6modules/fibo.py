
#fibonacci numbers module

def fib( n):
    a, b = 0,1
    while a < n:
        #end ='space'
        print( a, end=' ')
        a, b = b, a+b
    print()


def fib2( n):# return Fibonacci series up to n
    result = []
    a, b =0, 1
    while a < n:
        result.append( a)
        a, b = b , a+b
    return result

#2.如果这个模块被当作脚本（含main 的主文件）启动 的话，读取系统参数，执行下面的语句。这么写
if __name__ == "__main__":
    import sys
    fib( int( sys.argv[1] ))
#这么运行 python3 fibo.py 50
#将调用fib函数，打印前50个斐波那契数

#3. 这个文件当作模块时候，是不会执行上面的语句的3. 这个文件当作模块时候，是不会执行上面的语句的3. 这个文件当作模块时候(被imported)，是不会执行上面的语句的
