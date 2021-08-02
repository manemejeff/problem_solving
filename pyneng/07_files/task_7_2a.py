# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            if line.startswith('!'):
                continue
            elif any([item in ignore for item in line.split()]):
                continue
            else:
                print(line, end='')