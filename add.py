import json
import os
import re
import sys
from datetime import datetime, timedelta

import django
import requests
from requests_oauthlib import OAuth1Session  # OAuthのライブラリの読み込み

if os.path.exists('local.py'):
    from local import AT, ATS, CK, CS, SK
else:
    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    ATS = os.environ['ATS']

sys.path.append('jp10')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jp10.settings')
django.setup()

twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = 'https://scoresaber.com/api/players/?countries=jp'

res = requests.get(url).json()

from app.models import Ranking

# print(res)
ans = []
ssids = [r['id'] for r in res]
print(ssids)

past_ssids = Ranking.objects.order_by('date').reverse()[0]
print(past_ssids)
p0 = past_ssids.n0
p1 = past_ssids.n1
p2 = past_ssids.n2
p3 = past_ssids.n3
p4 = past_ssids.n4
p5 = past_ssids.n5
p6 = past_ssids.n6
p7 = past_ssids.n7
p8 = past_ssids.n8
p9 = past_ssids.n9

past = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]

txt = ''

def get_name(id_num):
    url = f'https://scoresaber.com/api/player/{id_num}/basic'
    res = requests.get(url).json()
    try:
        return res['name']
    except:
        return '！名前取得エラー！'


for i in range(10):
    if ssids[i] == past[i]:
        continue
    else:
        past_id = past[i]
        new_id = ssids[i]
        past_name = get_name(past_id)
        new_name = get_name(new_id)
        txt += f'#{i+1} {past_name} -> {new_name}\n'

if txt != '':
    tweet_content = ''
    tweet_content += '日本TOP10に変動があったかも！\n'
    tweet_content += txt
    tweet_content = tweet_content[:140]
    url = "https://api.twitter.com/1.1/statuses/update.json" #ツイートポストエンドポイント
    print(tweet_content)
    params = {"status" : tweet_content}
    res = twitter.post(url, params = params) #post送信

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

