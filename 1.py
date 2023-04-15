# import sys
# import os
# import re
# from urllib.request import urlopen
#
# from ipwhois import IPWhois
# from prettytable import PrettyTable
#
# regex_as = re.compile("[Oo]riginA?S?: *([\d\w]+?)\n")
# regex_country = re.compile("[Cc]ountry: *([\w]+?)\n")
# regex_provider = re.compile("mnt-by: *([\w\d-]+?)\n")
#
#
# def trace(hostname):
#     cmd_line = f"tracert {hostname}"
#     result = os.popen(cmd_line).read()
#     return re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", result)
#
#
# def trace(hostname):
#     cmd_line = f"tracert {hostname}"
#     result = os.popen(cmd_line).read()
#     stdout = result.read()
#     # for i in result.split('\n'):
#     #     if 'ms' in i:
#     #         return i.split()[-1].rstrip('[]')
#     return re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", result)
#
#
# def parse(site, regex):
#     try:
#         result = regex.findall(site)
#         return result[0]
#     except:
#         return ''
#
#
# def is_grey_ip(ip):
#     return (
#             ip.startswith('192.168.') or
#             ip.startswith('10.') or
#             (ip.startswith('172.') and 15 < int(ip.split('.')[1]) < 32)
#     )
#
#
# def info_ip(ip):
#     if is_grey_ip(ip):
#         return ip, '', '', ''
#     url = f"https://www.nic.ru/whois/?searchWord={ip}"
#     try:
#         # ipwhois_data = IPWhois(ip).lookup_rdap()
#         # return ip, ipwhois_data['asn'], ipwhois_data['asn_country_code'], ipwhois_data['network']['name']
#         with urlopen(url) as f:
#             site = f.read().decode('utf-8')
#             return ip, parse(site, regex_as), parse(site, regex_country), parse(site, regex_provider)
#     except:
#         return ip, '', '', ''
#
#
# class TraceAS:
#     headers = ["№", "IP", "AS", "Страна", "Провайдер"]
#
#     def run(self, hostname):
#         ips = trace(hostname)
#         table_str = self.make_table(ips)
#         return table_str
#
#     def make_table(self, ips):
#         table = PrettyTable(self.headers)
#         for i, ip in enumerate(ips):
#             info = info_ip(ip)
#             table.add_row([i, *info])
#         return str(table)
#
#     @staticmethod
#     def check_args():
#         if len(sys.argv) != 2:
#             print('Input error')
#             sys.exit(1)
#
# if __name__ == "__main__":
#     trace_as = TraceAS()
#     trace_as.check_args()
#     trace_as.run(sys.argv[1])
