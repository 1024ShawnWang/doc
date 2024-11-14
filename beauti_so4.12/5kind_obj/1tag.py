from bs4 import BeautifulSoup


#1.只包含四种对象 Tag, NavigableString, BeautifulSoup, Comment

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
type(tag)# <class 'bs4.element.Tag'>

#2. Tag对象，最重要的两个name(名称)和attributes(属性)
print( tag.name) #u'b' #2.1 每个tag都有一个名字 ,可能相同

#3. 属性(包括name和attributes可以更改，会被相关联的对象记忆，并且影响后续结果

#4. 出现在闭合标签左边标签里面的，含有'='的会被识别为attributes
#4.1 可以通过. 或者字典那样，读取，写入attr中key对应的value
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
tag['id']# 'boldest'

print( tag.attrs)# {'id': 'boldest'} #4.2展示了如何取出所有 attributes，返回一个字典

tag['id'] ='verybold' #4.3修改id对应的value 
print( tag)

tag['another-attr']=1 #4.4 增加 k-v
print( tag)

del tag['id'] #4.5删除一对k-v
print( tag)

#print( tag['id']) #4.6没有此属性，返回KeyError，抛出异常

print( tag.get('id')) #4.7相同，不过get方法返回None


####多值attributes

#5.在新的html语言中，运行k-v中的v是多个值，此时，把这多个值封成列表
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print( css_soup.p['class']) # ['body', 'strikeout'] #返回一个列表，其实是k-v中的v


#6. 在构造方法中使用 multi_valued_attributes=None，强制使用单值解析
no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
print( no_list_soup.p['class'] ) # 'body strikeout'

#7. 强制所有都使用多值解析，可以使用get_attribute_list()方法
id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print( id_soup.p.get_attribute_list('id') )#返回['my','id']

#8.指定xml解析器，就没有多值
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']# 'body strikeout'

#9.默认使用的html标准，单值清晰，多值的话，k-v中的v变成列表
