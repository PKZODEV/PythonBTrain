import connectionDb
userInput = ''

def condition():
    global userInput
    print('1 select: ')
    print('2 insert: ')
    print('3 update: ')
    print('4 delete: ')
    if userInput == 1:
        connectionDb.select_data()
    elif userInput == 2:
        connectionDb.insert_data()
    elif userInput == 3;
        connectionDb.
    