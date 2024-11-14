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


# .next_element 指向下一个可解析对象，对比它和next_sibling，
last_a_tag = soup.find("a", id="link3")
print( last_a_tag) #<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
print( last_a_tag.next_sibling) # '; and they lived at the bottom of a well'
print( last_a_tag.next_element)  # 'Tillie' #1. 直接进入下一个元素中，类比 .contents[0]
print( last_a_tag.contents) #返回一个列表，虽然类不相同，但是内容是一样的


print( last_a_tag.previous_element) #2. .previous_element #对比 .parent，有很大不同 #对比previous_sibling，这里面一样，但是是不一定的
print( last_a_tag.previous_sibling)


#3. next_elements  #对比 next_siblings 和 previous_siblings

#4. previous_elements
