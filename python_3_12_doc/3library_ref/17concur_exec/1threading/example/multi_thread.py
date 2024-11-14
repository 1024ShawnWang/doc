import blog_spider
import threading
import time

def single_thread():
    print('单线程开始时间: ',time.time())
    for url in blog_spider.urls:
        blog_spider.craw( url)
    print('单线程结束时间: ',time.time())
    
def multi_thread():
    print('多线程开始时间: ',time.time())
    threads =[] #存放thread对象
    for url in blog_spider.urls:
        threads.append( threading.Thread( target=blog_spider.craw, args=(url,))) #添加线程对象
    
    for thread in threads: 
        thread.start() #调用start方法开始运行线程，至于线程真正什么时候启动全看系统调度

    for thread in threads:
        thread.join() #阻塞主线程，直到调用join()办法的子线程结束（让它爹等等它)
    print('多线程结束时间: ',time.time())


if __name__=='__main__': #如果这个文件被作为脚本文件直接执行了的话
    start =time.time()
    single_thread()
    end =time.time()
    print( '单线程花费了 ', end-start, 's')

    start =time.time()
    multi_thread()
    end =time.time()
    print( '多线程花费了 ', end-start, 's')

#看一下输出结果在 a.txt中， 前者花费6.54，后者花费0.26，提升了25倍
