# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

import sys
txt = ''
if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            # if line.startswith('!'):
            #     pass
            if any([item in ignore for item in line.split()]):
                continue
            else:
                txt += line
    with open('config_sw1_cleared.txt', 'w') as targ:
        targ.write(txt)
