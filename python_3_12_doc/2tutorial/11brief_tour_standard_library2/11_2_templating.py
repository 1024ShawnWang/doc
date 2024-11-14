from string import Template
t = Template('${village}folk send $$10 to $cause.') #1.使用${}来代表变量，这和shell何其相似
s =t.substitute( village='Xuzhou', cause='ditch fund')
print( s)

#2. substitute会抛出KeyError如果有的占位符没有被填充。 因此safe_substitute()更被推荐，它会保留占位符，如果没有替成功

#子类还可以指定分隔符delimiter
import time, os.path
photofiles =['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename( Template):
    delimiter='%' #3.重写类，来指定分隔符

fmt =input('Enter rename style(%d-date %n-seqnum %f-format): ') #eg: %d%n%f


t =BatchRename( fmt) #batchRename将占位符（或者说shell中变量的标志符改为了%)

date =time.strftime( '%d%b%y') #day 简写月 year

for  i, filename in enumerate( photofiles):
    base, ext =os.path.splitext( filename)#按照扩展名分割文件名
    newname =t.substitute(d=date, n=i, f=ext)#注意fmt格式，其中占位符因为batch改为了%
    print( '{0}-->{1}'.format( filename, newname) )#格式化输出

#好像还是没搞很懂
