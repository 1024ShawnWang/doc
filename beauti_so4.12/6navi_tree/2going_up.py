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

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
#print( soup.prettify())

#1.每个tag都有父节点，可以通过 .parent 属性来获取   
title_tag =soup.title

print( title_tag)
print( title_tag.parent) # 1. tag的 .parent属性

print( soup.parent) # BeautifulSoup对象的parent是None


link =soup.a #取出第一个<a>..</a>
for parent in link.parents: #2. 向上一直递进，不包括本身
    if parent is None:
        print( parent) #print( None)代表无输出
    else:
        print( parent.name)

#如果看不清父类，记得用 prettify()方法格式化一下
