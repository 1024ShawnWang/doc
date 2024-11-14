import requests

#urls =[ f"https://www.cnblogs.com/#p{page}", for page in range(1, 50+1)]
#报错 syntaxError: did you forget parentheses around the comprehension target?

urls =[ f'https://www.cnblogs.com/#p{page}' for page in range(1, 50+1)]
#单引号是可以的

#print( urls)

def craw( url):
    r = requests.get( url)
    print( url, len( r.text))

craw( urls[0])


