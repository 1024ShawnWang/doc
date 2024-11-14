import re

def displaymatch( match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' %(match.group(), match.groups())

valid =re.compile( r'^[a2-9tjqk]{5}$')
print( displaymatch( valid.match('akt5q')) )


#匹配对子，好厉害，我怎么看不懂
pair = re.compile( r'.*(.).*\1')  #看不懂思密达，好像是必须和()配合使用
print( pair.match('717ak').group(1) )

#词法分析器
from typing import NamedTuple
import re

class Token( NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize( code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification=[
            ('NUMBER', r'\d+(\.\d*)?'),
            ('ASSIGN', r':='),
            ('END', r';'),
            ('ID',  r'[A-Za-z]+'),
            ('OP',  r'[+\-*/]'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.'),
            ]

    tok_regex= '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_num=1
    line_start=0

    for mo in re.finditer( tok_regex, code):
        kind =mo.lastgroup
        value =mo.group()
        column =mo.start()-line_start
        if kind =='NUMBER':
            value= float( value) if '.' in value else int( value)
        elif kind=="ID" and value in keywords:
            kind=value
        elif kind =="NEWLINE":
            line_start =mo.end()
            line_num +=1
            continue
        elif kind =="SKIP":
            continue
        elif kind =="MISMATCH":
            raise RuntimeError(f'{value!r} unexpcected on line {line_num}')
        yield Token( kind, value, line_num, column)

statements='''
    IF quantity THEN
        total := total + price*quantity;
        tax := price *0.85
    ENDIF;
'''

for token in tokenize( statements):
    print( token)

#看不懂思密达
