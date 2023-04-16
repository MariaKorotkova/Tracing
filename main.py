import sys
import os
from ipwhois import IPWhois
from prettytable import PrettyTable


def get_ip(name):
    """Функция получения ip-адреса, с помощью утилиты tracert"""
    result = os.popen(f"tracert {name}").read()
    list_ip = list()
    for i in result.split('\n'):
        if 'ms' in i:
            list_ip.append(i.split()[-1].strip('[]'))
    return list_ip


def get_ip_information(ip):
    """Функция получения информации об ip-адресах
    Проверка на серые адреса: если адрес серый, то в таблице записывается '-'
    """
    if ip.startswith('192.168.') or ip.startswith('10.') or (ip.startswith('172.') and 15 < int(ip.split('.')[1]) < 32):
        return ip, '-', '-', '-'
    try:
        ipwhois_data = IPWhois(ip).lookup_rdap()
        return ip, ipwhois_data['asn'], ipwhois_data['asn_country_code'], ipwhois_data['network']['name']
    except:
        return ip, '', '', ''


def make_table(ips):
    """Создание таблице с данными об ip-адресах"""
    table = PrettyTable(["№", "IP", "AS Name", "Country", "Provider"])
    for i, ip in enumerate(ips):
        info = get_ip_information(ip)
        table.add_row([i, *info])
    return table


def main():
    """Запуск программы в терминале: .\main.py ip-адрес или доменное имя """
    if len(sys.argv) == 2:
        ip = get_ip(sys.argv[1])
        print(make_table(ip))


if __name__ == '__main__':
    main()
