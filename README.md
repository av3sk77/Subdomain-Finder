# Subdomain-Finder
Subdomain Finder is a python script designed to enumerate the subdomains of websites Using Subdomain Brute Force. This script will help for Web Penetration Testing. You can get Subdomains of your Target Domain. You have to provide the <b>domain name</b> of target domain. If you Don't provide the subdomain list it will be use default 1000 word subdomain list. If you want to get output in file so you can get see in Help Menu.

## Requirement
You must be Install Python3 Version<br/>
### Install the Dependency
```
pip3 install dnspython
```

### Help Menu
```bash
# python3 subdomain-finder.py -h

usage: subdomain-finder.py [-h] [-o OUT] [-s SUBDOMAIN] -d DOMAIN

optional arguments:
  -h, --help    show this help message and exit
  -o OUT        Output File [Ex. -o "found.txt"]
  -s SUBDOMAIN  SubDomains List [Ex. -s "/root/Desktop/SubDomains.txt"]

Required Arguments:
  -d DOMAIN     Domain Name [Ex. -d google.com]
```


### Usage
#### Run Script
```bash
# python3 subdomain-finder.py -d google.com
```
#### With Subdomain List
```bash
# python3 subdomain-finder.py -d google.com -s subdomains.txt
```
#### Get Output in File
```bash
# python3 subdomain-finder.py -d google.com -s subdomains.txt -o found.txt
```
