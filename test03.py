# File Handing
#ไฟล์ การจัดการ
#คือ การทำงานเก็บไฟล์
#การเปิดไฟล์ write (w)/extend (x)/read (r)

f_iot = open('iot3.txt', 'x', encoding = 'utf-8')

f_iot.write('Wow.....')
f_iot.write('Hi....\n')
f_iot.write('สวัสดี.....\n')

f_iot.clonclose()