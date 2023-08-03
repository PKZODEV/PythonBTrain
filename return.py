import os

userInput = ''
def main():
    while True:
        global userInput
        print('select menu ')
        print('1.show name folder')
        print('2.mutiply')
        print('3.End')
        userInput = int(input('choose Topic: '))
        if userInput == 1:
            showfolder()
        elif userInput == 2:
            showmutiply()
        elif userInput == 3:
            break


def showfolder():
    for NameDir in os.listdir('c:\\'):
        print(NameDir)

def showmutiply():
    usernum = int(input('enter number : '))
    number = 1
    while number<12:
        print('%d * %d = %d'%(usernum,number,(usernum*number)))
        number += 1


main()
