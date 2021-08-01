# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

if __name__ == '__main__':
    print(mac.replace(':', '.'))