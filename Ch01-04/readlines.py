f = open("./newFile.txt",'r')
lines = f.readlines()
for i in lines:
    print(i,end = '')
f.close()
