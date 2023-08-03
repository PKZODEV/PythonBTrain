filewrite = open('test.txt','a')
filewrite.write('hello quick\n')
filewrite.write('this is a book\n')
filewrite.write('this is a dog\n')
filewrite.write('this is a cat\n')
filewrite.write('this is a color\n')
filewrite.close()

readfile = open('test.txt','r')
for line in readfile:
    print(readfile)