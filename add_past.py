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

import csv

from app.models import Ranking

f = open('past_top10.csv','r')
reader = csv.reader(f)
next(reader)
for r in reader:
    print(r)
    ymd = list(map(int,r[0].split('-')))
    print(ymd)
    date = datetime(ymd[0],ymd[1],ymd[2],12,0,0)
    Ranking.objects.create(
        date = date,
        n0 = r[1],
        n1 = r[2],
        n2 = r[3],
        n3 = r[4],
        n4 = r[5],
        n5 = r[6],
        n6 = r[7],
        n7 = r[8],
        n8 = r[9],
        n9 = r[10],
    )

