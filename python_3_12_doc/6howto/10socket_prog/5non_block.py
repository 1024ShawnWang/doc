###########################
#非阻塞的套接字

#1. 在python中，使用 socket.setblocking( False)来设置非阻塞

#2. 非阻塞的意思就是： send, recv, connect, accept 可以在***没有做任何事情***的情况下返回

#3. 使用 select库
#3.1 下面的不看了
