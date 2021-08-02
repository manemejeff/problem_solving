# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

if __name__ == '__main__':
    while True:
        ip = input('Enter IP format X.X.X.X: ')
        try:
            if len(ip.split('.')) != 4:
                # print('Format')
                print('Неправильный IP-адрес. Введите адрес повторно')
                continue
            elif any([int(item) > 255 for item in ip.split('.')]):
                # print('Number')
                print('Неправильный IP-адрес. Введите адрес повторно')
                continue
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
                break
        except Exception as e:
            print('Неправильный IP-адрес. Введите адрес повторно')
            continue
