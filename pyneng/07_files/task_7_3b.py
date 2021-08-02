# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import sys

if __name__ == '__main__':
    cams = []
    vlan = sys.argv[1]
    with open('CAM_table.txt') as f:
        for line in f:
            if line.count('.'):
                cams.append(line)
    for line in cams:
        if line.split()[0] == vlan:
            print(line, end='')
