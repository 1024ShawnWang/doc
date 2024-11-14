html_doc= """
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

#
first_link = soup.a
print( first_link)

print(first_link.find_next_sibling()) #搜索下一个元素
print(first_link.next_sibling)  #看到了把，next_sibling确实是 ' 号，但是find_next_sibling有封装，估计是排除了这些字符串（非Tag)对象
