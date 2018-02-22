# -*- coding: utf-8 -*-
import sys
import io
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

keywords = ["의사","청초","이성","질서","지혜","서약","선량","절도","성실","생명","관용","해방","조화","창조","신뢰","전통","변화","결합","엄격","용기","행운","비호","치유","자애"]

def printCard(content,indent=' '):
    print('{0}------ '.format(indent))
    print('|      |')
    print('|{0:^4}|'.format(content))
    print('|      |')
    print(' ------ ')

#while True:
#    ans = input("새로운 값을 뽑으시겠습니까? (y/n) : ")
#    if ans == 'n' or 'N':
#        break
loop1 = 0
select = []
while loop1 < 6:
    p1 = [keywords[random.randint(0,23)]]
    tmp = random.randint(0,1)
    if tmp == 0 :
        p2 = '*'
    else :
        p2 = ' '
    select.append([p1,p2])
    loop1 += 1
#print Start
while loop1 > 0:
    [p1,p2] = select.pop()
    print(p1)
    printCard(p1,p2)
    loop1 -= 1
