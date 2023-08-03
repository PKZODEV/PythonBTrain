usernum = int(input('enter num: '))
for i in range(12):
    for test in range(1,12+1):
        total = usernum * test
        print('%d * %d = %d'%(usernum,test,total))
    usernum += 1