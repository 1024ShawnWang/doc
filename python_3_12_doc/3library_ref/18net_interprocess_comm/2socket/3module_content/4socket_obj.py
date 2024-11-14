#socket对象，有以下方法 ( socket可能工作在 传输层，下面就是需要ip的网络层)

#1. socket.accept() 接收一个连接。此socket必须绑定到一个地址上，并且监听连接。返回值是一个 (conn,address)
#其中 conns 是一个 新的 套接字对象， 并于此连接 上，收发数据， address 是连接另一端的套接字所绑定的地址

#2. socket.bind( address) 将套接字绑定到 address。 套接字必须尚未绑定

#3. socket.close() 关闭套接字。

#4. socket.connect( address) #连接到address处的 远程套接字

#5. socket.connect_ex( address)

#6. socket.detach() #将套接字对象置于 关闭 状态，返回该文件描述符

#7. socket.dup() #复制该套接字

#8. socket.fileno() #返回套接字的文件描述符（一个小整数），f失败返回-1

#9. socket.get_inheritable() #s获取套接字文件描述符，或 套接字句柄 的 可继承标志

#10. socket.getpeername() #返回套接字连接到的远程地址。 所谓的peer就是 客户端---服务器

#11. socket.getsockname() f返回套接字本身的地址

#12. getsockopt( level, optname[, buflen]) 

#13. getblocking() #如果套接字处于阻塞模式，就返回 True

#14. gettimeout()

#15. ioctl( control, option) #只能在windows平台使用

#16. listen( [backlog]) #启用一个服务器用于接收连接 ,backlog是最大连接数，不指定的话就是默认值

#17. makefile( mode='r', buffering=None, *, encoding=None, errors=None, newline=None) #返回一个与套接字相关联的 file object

#18. recv( bufsize[, flags]) #从套接字接收数据。返回值是一个代表所接受数据的字节串对象

#19. recvfrom( bufsize[, flags]) 从套接字接收数据，返回值是一对 ( bytes, address)

#20. recvmsg( bufsize[, ancbufsize[, flags]])

#21. recvfrom_into( buffer[, nbytes[, flags]])

#22. recv_into( buffer[, nbytes[, flags]])

#23. send( bytes[, flags]) #发送数据给套接字。本套接字必须已经连接到远程套接字

#24. 剩下的省略了，用到再说吧，爷累了 10/25/24

