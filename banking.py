balance = 1000
userInput = ''

def main():
    while True:
        global userInput
        print('========Quick Banking========\n========Mobile Saving========')
        print('========เลือกเมนูที่ต้องการ========')
        print('1.ดูยอดเงินปัจจุบัน')
        print('2.ถอนเงิน')
        print('3.สินเชื่อ')
        print('4.ลงทุน')
        print('5.จบการทำงาน')
        userInput = int(input('กรุณากรอกเมนูที่คุณต้องการ: '))
        print('=============================')
        if userInput == 1:
            print(balance)
        if userInput == 2:
            withdraw()
        if userInput == 3:
            credit()
        if userInput == 4:
            savings()
        if userInput == 5:
            break

def withdraw():
    withdraws = int(input('กรุณากรอกจำนวนเงินที่ต้องการถอน: '))
    print('จำนวนเงินที่ท่านต้องการถอนคือ %d'%withdraws)
    total = balance - withdraws
    print('ยอดเงินคงเหลือคือ %d'%total)

def credit():
    credits = int(input('กรุณากรอกจำนวนเงินสินเชื่อที่ท่านต้องการ: '))
    print('จำนวนสินเชื่อที่ท่านต้องการกู้คือ: %d'%credits)
    print('ทำรายการกู้สินเชื่อสำเร็จแล้ว')
    print('ยอดเงินของท่านคือ %d'%(balance+credits))

def savings():
    saving = int(input('กรุณากรอกจำนวนเงินที่ท่านต้องการลงทุน: '))
    print('จำนวนเงินที่ท่านต้องการลงทุนคือ: %d', saving)
    print('ทำรายการสำเร็จแล้ว')
    print('นี่คือดอกเบี้ยนโดยประมาณที่ต้องจะได้ %5 ของยอดเงินลงทุนของทุกเดือน')
    for i in range(1,12+1):
        average = saving * 5 / 100
        print('เดือนที่ %d ยอดเงินลงทุน: %d ดอกเบี้ยที่ได้: %d'%(i,saving,average))


main()

