userInput = ''

def main():
    global userInput
    print('พี่มีจดหมายอยู่หนึ่งฉบับที่อยากจะให้อ้อนลองอ่าน')
    print('อยากลองอ่านไหม')
    print('1.เปิด')
    print('2.ไม่เปิด')
    userInput = int(input('เปิดไหม เปิดพิมพ์ 1 ไม่เปิดพิมพ์ 2: .....'))
    if userInput == 1:
        openletter()
    if userInput == 2:
        print('โอเค....')

def openletter():
    aonInput = ''
    print('ขอบคุณนะที่ยังรักกันและยังพาพี่มาอยู่ด้วยกันอีกไม่ว่าอะไรจะเปิดขึ้นพี่จะไม่ทิ้งอ้อนไปไหน\nรักมากๆเลยอยากอยู่ด้วยกันตลอดอยูุ่ด้วยกันไปนานๆ '
          'ขอให้ทุกอย่างยังคงไม่เปลี่ยนไปและไม่จากไปไหนนะ ยังคงรู้สึกเหมือนวันแรกที่เจอเสมอรักมาขึ้นทุกๆวัน ')
    print('แล้วอ้อนหล้ะรักพี่ไหม?')
    aonInput = int(input('ถ้ารักพิมพ์ 1 ไม่รัก พิมพ์ 2:....'))
    if aonInput == 1:
        print('จุ๊บ รักนะครับที่รัก')
    if aonInput == 2:
        print('แงๆๆ เสียใจจัง')

main()