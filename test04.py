# File Handing
#ไฟล์ การจัดการ
#คือ การทำงานเก็บไฟล์
#การเปิดไฟล์ write (w)/extend (x)/read (a)/read (r)

f_iot = open('iot3.txt', 'a', encoding = 'utf-8')

f_iot.write('1111....')
f_iot.write('222..\n')
f_iot.write('333.....\n')

f_iot.clonclose()