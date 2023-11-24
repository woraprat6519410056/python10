f_iot = open('iot3.txt', 'a', encoding = 'utf-8')

data = f_iot.readline()
print(data, end='')
data = f_iot.readline()
print(data, end='')
data = f_iot.readline()
print(data, end='')
data = f_iot.readline()
print(data, end='')

f_iot.close()