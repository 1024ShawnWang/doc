mport socket

HOST = 'daring.cwi.nl'    # 远端主机
PORT = 50007              # 与服务器所用端口相同
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
            data = s.recv(1024)
            print('Received', repr(data))

#这个程序在丑丑上有复制版，在丑丑上运行更方便直观，当然你可以登陆两次master，毕竟服务器程序会阻塞
