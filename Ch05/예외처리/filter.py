# -*- coding: utf-8 -*-
# positive.py
'''
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))
'''
'''
def positive(x):
    return x > 0

print(list(filter(positive,[1,-3,2,0,-5,6])))

'''

#Using with lambda and filter func

print(list(filter(lambda a:a>0,[1,-3,2,0,-5,6])))
