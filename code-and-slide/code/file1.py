myfile = open('test.txt')
lines = myfile.readlines()
myfile2 = open('new.txt','w')
for i in range(len(lines)-1, -1, -1):
    myfile2.write(lines[i])
myfile.close()
myfile2.close()
