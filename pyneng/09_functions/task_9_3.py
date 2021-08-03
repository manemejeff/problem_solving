# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config_filename: str):
    ports_acces = {}
    ports_trunk = {}
    txt = ''
    interface, mode, vlan = None, None, None
    with open(config_filename) as f:
        for line in f:
            if 'interface' in line:
                mode, vlan = None, None
                interface = line.split()[1]
            if 'switchport mode' in line:
                mode = 'trunk' if 'trunk' in line else 'access'
            if 'vlan' in line:
                vlan = line.split()[-1]
            if all([interface, mode, vlan]):
                if mode == 'trunk':
                    ports_trunk[interface] = vlan.split(',')
                else:
                    ports_acces[interface] = vlan

    return ports_acces, ports_trunk


if __name__ == '__main__':
    print(get_int_vlan_map('config_sw1.txt'))
