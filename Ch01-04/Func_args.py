def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_many(1,2,3,4,5,6,7))

#C언어와 마찬가지로, 함수를 나중에 선언하면 에러가 발생한다.
'''
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
'''
