from bs4 import BeautifulSoup # as bs

#注意是三个双引号
html_doc = """ 
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup( html_doc, 'html.parser') #1. 传入html，返回一个BeautifulSoup对象

print( soup.prettify()) #2. 返回一个格式化的嵌套结构

print( soup.title) #3. 返回 <title>The Dormouse's story</title>，用.的办法直接取出来第一个碰到的对象

print( soup.title.name) #4. title Tag对象有name属性

print( soup.title.string) #5. u'The Dormouse's story' 返回tag包围的字符串

#6. u'hello world' 表示 'hello world'是 unicode字符串

print( soup.p) #<p class="title"><b>The Dormouse's story</b></p>

print( soup.p['class']) #6 ['title']  6.1返回一个列表, 6.2注意 class在 闭合标签的左标签内
print( type( soup.p['class'])) # <class list>

print( soup.find('a'))  #7.注意和find_all比较
print( soup.find_all('a')) #7.1返回一个列表

print( soup.find( id="link3")) #8.<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> #可以根据id查找


for link in soup.find_all('a'): #找到所有<a></a>标签中的链接，并输出
    #print( link.get('href'))  #9. 用了get方法，
    print( link['href'])  #6. 注意href的位置，和6用相同的办法


print( soup.get_text())  #10.输出所有文本。闭合标签内部的
