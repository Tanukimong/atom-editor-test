import sys

def printTuple(tup):
    i = 1
    for index in tup:
        print('{0}. {txt}'.format(i, txt = index))
        i += 1

num = 0

t1 = ('Kozakura Mary', 'Zero','Amami Haruka','Onodera Kosaki','Iijama Yun','Mio','none')

while True:
    print('{txt:=^16}'.format(txt = 'Who is your wife?'))
    printTuple(t1)
    num = int(input('Input : '))
    if t1[num-1] is 'none' :
        sys.exit()
    print('----------------------')
    print(t1[num-1] + "? really?")
    print('----------------------')
