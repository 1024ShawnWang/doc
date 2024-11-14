from dataclasses import dataclass

@dataclass  #1. 类比c语言中的Struct
class Employee:
    name: str
    dept: str
    salary: int

john= Employee('john', 'computer job', 1000)

print( john.dept)
