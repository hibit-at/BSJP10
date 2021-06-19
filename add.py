import json
import os
import re
import sys
from datetime import datetime, timedelta

import django
import requests

sys.path.append('jp10')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jp10.settings')
django.setup()

url = 'https://scoresaber.com/global/1&country=jp'

get = requests.get(url)
txt = get.text.replace('\n', '').replace('\t', '')

from app.models import Ranking

pattern = r'<span class="songTop pp" style="font-weight: 700;">(.*?)</span>'
names = re.findall(pattern, txt)
# print(names)
pattern = r'<td class="player"><a href="/u/(.*?)">'
ssids = re.findall(pattern, txt)
# print(ssids)

ans = []

from datetime import datetime

now = datetime.now()

Ranking.objects.create(
    date=now,
    n0 = ssids[0],
    n1 = ssids[1],
    n2 = ssids[2],
    n3 = ssids[3],
    n4 = ssids[4],
    n5 = ssids[5],
    n6 = ssids[6],
    n7 = ssids[7],
    n8 = ssids[8],
    n9 = ssids[9],
)

