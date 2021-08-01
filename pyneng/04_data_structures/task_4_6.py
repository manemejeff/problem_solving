# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

if __name__ == '__main__':
    data = ospf_route[1:].strip().split()

    protocol = 'OSPF'
    prefix = data[0]
    ad_metric = data[1].strip('[]')
    next_hop = data[3].strip(',')
    last_update = data[4].strip(',')
    outbound_interface = data[5]
    leng = 23
    spc = ' '

    protocol_str = 'Protocol:'
    prefix_str = 'Prefix:'
    ad_metric_str = 'AD/Metric:'
    next_hop_str = 'Next-Hop:'
    last_update_str = 'Last update:'
    outbound_interface_str = 'Outbound Interface:'

    answer = f'{protocol_str}{spc*(leng-len(protocol_str))}{protocol}\n' \
             f'{prefix_str}{spc*(leng-len(prefix_str))}{prefix}\n' \
             f'{ad_metric_str}{spc*(leng-len(ad_metric_str))}{ad_metric}\n' \
             f'{next_hop_str}{spc*(leng-len(next_hop_str))}{next_hop}\n' \
             f'{last_update_str}{spc*(leng-len(last_update_str))}{last_update}\n' \
             f'{outbound_interface_str}{spc*(leng-len(outbound_interface_str))}{outbound_interface}\n'

    print(answer)