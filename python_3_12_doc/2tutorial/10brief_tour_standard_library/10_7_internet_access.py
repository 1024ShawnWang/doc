
#两个最简单的函数用来从网上取得数据和发送邮件，分别是

from urllib.request import urlopen

#下面的没加http://导致了出错
#with urlopen('www.baidu.com') as response:
with urlopen('http://www.baidu.com') as response:
    for line in response:
        line = line.decode() #将字节流解码成字符串
        #print( line)        #暂时不输出了，为了下面的模块


import smtplib
server =smtplib.SMTP('localhost') #需要本机开启smtp服务
server.sendmail('Tutu@Moon.org', '1192877628@qq.com',
        """To: 1192877628@qq.com
        From: Tutu@Moon.org

        Report Ip from Tutu: 112.84.85.80
        """)
server.quit()
#报错，连接被拒绝❌
