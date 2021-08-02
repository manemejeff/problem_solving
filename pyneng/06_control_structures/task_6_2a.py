# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

if __name__ == '__main__':
    ip = input('Enter IP format X.X.X.X: ')

    if len(ip.split('.')) != 4:
        print('Format')
        print('Неправильный IP-адрес')
    elif any([int(item) > 255 for item in ip.split('.')]):
        print('Number')
        print('Неправильный IP-адрес')
    else:
        if 1 <= int(ip.split('.')[0]) <= 223:
            print('unicast')
        elif 224 <= int(ip.split('.')[0]) <= 239:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
