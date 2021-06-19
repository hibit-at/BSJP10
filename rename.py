import re
import urllib.error
import urllib.request

import requests

url = 'https://scoresaber.com/global/1&country=jp'

get = requests.get(url)
txt = get.text.replace('\n', '').replace('\t', '')


pattern = r'<span class="songTop pp" style="font-weight: 700;">(.*?)</span>'
names = re.findall(pattern, txt)
# print(names)
pattern = r'<td class="player"><a href="/u/(.*?)">'
ssids = re.findall(pattern, txt)
# print(ssids)

match = {}

for n,s in zip(names,ssids):
    match[n] = s

import os

root = 'static'
LD = os.listdir(root)

for L in LD:
    name = L[:-4]
    print(name)
    if name in match:
        print('match!')
        before = os.path.join(root,L)
        after = os.path.join(root,f'{match[name]}.jpg')
        os.rename(before,after)
