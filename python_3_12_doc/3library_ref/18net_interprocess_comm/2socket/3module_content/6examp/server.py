
#Echo server program

import socket

HOST = ''
PROT = 50007

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind( (HOST, PROT))
    s.listen( 1) #最大连接数为1
    conn, addr = s.accept() # 服务器不是在监听的连接上，发送数据，而是通过accept() 新建一个 套接字对象，发送数据
    with conn:
        print( 'Connected by', addr)
        while True:
            data =conn.recv( 1024)
            if not data: break #数据为空，就中断这个循环
            conn.sendall( data) #返回给客户端
