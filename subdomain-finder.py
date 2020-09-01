print('''
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
''')

# Script Title: Subdomains-finder
# SubDomain Brute Force Script
# Date: 31-08-2020
# Help Menu- python3 subdomain-finder.py -h
# Script Usage- python3 subdomain-finder.py -d google.com -s subdomains.txt
#!/usr/bin/python3

from pathlib import Path
import dns.resolver
import argparse
import requests
import threading
import sys

print('Made By- Aves Ahmed Khan')
print('')
print('If You Have Any Query PM me at:')
print('Twitter  - https://twitter.com/av3sk77')
print('LinkedIn - https://www.linkedin.com/in/aves-ahmed-khan-b835a7168/')
print('')


parser = argparse.ArgumentParser()
parser.add_argument("-o", dest="out", help='Output File [Ex. -o "found.txt"]')
parser.add_argument("-s", dest="subdomain", help='SubDomains List [Ex. -s "/root/Desktop/SubDomains.txt"]')

required = parser.add_argument_group('Required Arguments')
required.add_argument("-d", dest="domain", help='Domain Name [Ex. -d google.com]', required=True)

args = parser.parse_args()
out_file = args.out
domain_name = args.domain

if args.subdomain is None:
    sub_domains = "default.txt"
elif not Path(args.subdomain).exists() & Path(args.subdomain).is_file():
    print("Sub-Domains File Not Found:", args.subdomain)
    sys.exit()
else:
    sub_domains = args.subdomain

server = dns.resolver.Resolver()
server.nameservers = ['8.8.8.8']

def check(list, domain_name):
    try:
        fdomain = f"{list}.{domain_name}"
        dnsans = server.query(fdomain, 'A')

    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        pass
    except (dns.name.EmptyLabel, dns.name.LabelTooLong):
        pass
    else:
        for rdata in dnsans:
            print(f"{fdomain} is Found")
            if out_file is not None:
                with open(out_file, 'a') as write_file:
                    write_file.write(list + "\n")
                    write_file.close()
                    
with open(sub_domains, 'r') as file:
    for list in file.read().splitlines():
        t = threading.Thread(target=check, args=(list, domain_name,))
        t.start()
