from ftplib import FTP

ftp=FTP('ftp.us.debian.org') #连接到主机，默认端口

ftp.login()     #匿名用户，无密码

ftp.cwd('debian') #改变到 debian 目录

ftp.retrlines('LIST') #列出目录

with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write)

ftp.quit()

# 取回了服务器上的  README 文件  (RETR  README是命令
# 很奇怪，写成脚本文件执行不了，但是换命令行可以
# 又可以了，估计是网络问题
# 想要逐条执行命令，可以考虑open() 和 exec() 命令组合
