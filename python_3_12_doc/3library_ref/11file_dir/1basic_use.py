from pathlib import  Path

p=Path('.')
print( [x for x in p.iterdir() if  x. is_dir() ] ) #1. 输出运行此文件所在目录的所有子目录

print( list(p.glob('**/*.py')) ) #2. 列出当前目录下，所有以.py结尾的文件

p = Path('/etc')
q = p/'init.d'/'reboot'  #3. 生成新的路径对象，（我觉得它的实现也就是换了一个，所以你看 分隔符没有引号包裹，换不同平台，加不同分隔符罢了）
print( q)
print (q.resolve() ) #4.变为绝对路径

print( q.exists() )# 5.检查是否存在


#6. exception pathlib.UnsupportedOperation  继承NotImplementedError异常
