# Original code by Rikatez.
# dont reselling this code

import os, requests as rikatez, requests.exceptions, platform, hashlib, time, base64, json, sys, random, importlib.util, datetime
from bs4 import BeautifulSoup as rk
rikatez.urllib3.disable_warnings()

O = '\x1b[m'
B = '\033[1m'
R = '\x1b[33;31;1m'
G = '\x1b[33;32;1m'
C = '\x1b[33;36;1m'
W = '\x1b[33;37;1m'
Y = '\x1b[33;33;1m'
logo = f''' {O}{B}{G}_____  _ _      _______{O}\n {O}{B}{W}|  __ \(_) |    |__   __|{O}\n {O}{B}{G}| |__) |_| | ____ _| | ___ ____ {O}\n {O}{B}{W}|  _  /| | |/ / _` | |/ _ \_  /{O}\n {O}{B}{W}| | \ \| |   < (_| | |  __// / _{O}\n {O}{B}{G}|_|  \_\_|_|\_\__,_|_|\___/___(_) {O}'''
log = 'Rikatez | Not Found.'

rkz = rikatez.Session()
url = 'https://www.behindthename.com/random/random.php?gender=m&number=2&sets=5&surname=&randomsurname=yes&showextra=yes&norare=yes&nodiminutives=yes&usage_afr=1&usage_eng=5'
ua = rikatez.get('https://gitlab.com/rikatezz/rika/-/raw/main/ua.txt', verify=False).text
hdr = { 'Host':'www.behindthename.com', 'User-Agent': random.choice(ua.split('\n')), 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Referer': '1087', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip'}
rkt = rk(rkz.get(url, headers=hdr, verify=False).text,'html.parser').findAll('a',{'class':'plain'})
otlk = [ 'outlook.com', 'hotmail.com', ]
rndom_otlk = random.choice(otlk)
url_pass = 'https://www.random.org/passwords/?num=5&len=15&format=html&rnd=new'
hider = { 'Host':'www.random.org', 'User-Agent': random.choice(ua.split('\n')), 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Referer': '1087', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip'}
pass_random = rk(rkz.get(url_pass, headers=hider, verify=False).text,'html.parser').find('ul',{'class':'data'}).findAll('li')
print(f'{rkt[0].text}{rkt[1].text}{rkt[2].text}'+f'@{rndom_otlk} {pass_random[0].text}')
print(f'{rkt[3].text}{rkt[4].text}{rkt[5].text}'+f'@{rndom_otlk} {pass_random[1].text}')
print(f'{rkt[6].text}{rkt[7].text}{rkt[8].text}'+f'@{rndom_otlk} {pass_random[2].text}')
print(f'{rkt[9].text}{rkt[10].text}{rkt[11].text}'+f'@{rndom_otlk} {pass_random[3].text}')
print(f'{rkt[12].text}{rkt[13].text}{rkt[14].text}'+f'@{rndom_otlk} {pass_random[4].text}')
