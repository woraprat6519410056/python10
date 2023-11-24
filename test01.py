#Exception Handling
#ข้อผิดพลาด การจัดการ
#Exception ข้อผิดพลาดที่เกิดขึ้นตอนโปรแกรมทำงาน
#try-except-finally

try : 
    num = int( input('ป้อนตัวเลขที่1 :'))
    num = int( input('ป้อนตัวเลขที่2 :'))

    sun = num1 + num2
    result = num1 / num2

    print(f'ผลรวมของ {num1} + {num2} คือ {sun}')
    print(f'ผลรวมของ {num1} / {num2} คือ {result}')
except ValueError :
    print('ป้อนตัวเลขเท่านั้นท้ายตัวอักษร....สงสัยติดต่อ IT')
except ZeroDivisionError :
    print('ป้อนตัวเลขที่ 2 ท้ายเป็น 0....สงสัยติดต่อ IT')
except Exception :
    print('มีข้อผิดพลาดเกิดขึ้น ต้องขออภัยอย่างสูง ช่วยติดต่อ IT ด้วยจะแก้ให้')
finally :
    print('Wow..')
    print('Hello...')