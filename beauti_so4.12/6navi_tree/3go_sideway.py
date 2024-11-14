from bs4 import BeautifulSoup

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
print(sibling_soup.prettify())


#1.所谓兄弟节点，就是在prettify()后，有相同缩进的tag。在上面， <b> 和 <c>就是兄弟节点 （sibling)


print( sibling_soup.b.next_sibling) #<c>  #2. next_sibling
print( sibling_soup.b.previous_sibling) #None
print( sibling_soup.c.previous_sibling) #<b> #3. previous_sibling


#4.实际文档中的 .next_sibling 和  previous_sibling属性常常是 换行符，下面举例
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print( soup.a.next_sibling) #',' #这里的逗号是 22行末尾的逗号, 而不是 <a....> Lacie</a>
print( soup.prettify()) #这一点，用prettify()可以看的非常清楚

#5. 去除22行的',' 并不会输出下个<a></a>这个tag，而是会输出空白

print( soup.a.next_sibling.next_sibling)  #6. 无论去不去除22行的逗号，都可以找到<a...>Lacie</a> ，神奇


for sibling in soup.a.next_siblings:  #7. next_siblings是一个下面兄弟节点的迭代器 ，对比 2, 类比 .parent和.parents
    print( repr(sibling) )

#8 .previous_siblings
