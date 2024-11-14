def average( values):
    """computer the average of a list of numbers.

    >>>print( average( [20, 30, 70]))
    40.0
    """
    return sum(values)/len(values)

import doctest #1. 自动测试模块
doctest.testmod()
#没弄懂思密达，不过知道有这么一个东西就行了

#2. 还有一个unittest模块，更加精细
