import json
import requests
import sys
import os
import django

sys.path.append('jp10')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jp10.settings')
django.setup()

from app.models import PCRanking

def json_tree(data,indent=0):
    space = ' '*indent
    if type(data) == dict:
        for k in data.keys():
            print('\n',space,k,end='')
            json_tree(data[k],indent+4)
    elif type(data) == list and len(data) > 0:
        json_tree(data[0],indent+4)
    else:
        print(' :',data,end='')
    return

for page in range(1,51):
    print(f'page{page} searching')
    url = f'https://scoresaber.com/api/players?page={page}&countries=JP'
    res = requests.get(url).json()
    # json_tree(res)
    sids = [p['id'] for p in res['players']]
    playcounts = [p['scoreStats']['totalPlayCount'] for p in res['players']]
    names = [p['name'] for p in res['players']]
    profilePictures = [p['profilePicture'] for p in res['players']]
    zips = list(zip(sids,playcounts,names,profilePictures))
    for sid,playcount,name,profilePicture in zips:
        defaults = {
            'playcount' : playcount,
            'name' : name,
            'profilePicture' : profilePicture,
        }
        PCRanking.objects.update_or_create(
            sid = sid,
            defaults = defaults,
        )
