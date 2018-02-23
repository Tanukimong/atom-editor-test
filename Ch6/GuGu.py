# -*- coding: utf-8 -*-

def GuGu(num):
    i = 0
    result = []
    while i < 9:
        i += 1
        result.append(num*i)
    return result


result = GuGu(2)
j = 0
bigResult = []
while j<9:
    j+=1
    bigResult.append(GuGu(j))
print(bigResult)
