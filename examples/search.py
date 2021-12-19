#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from bluebird import BlueBird

query = {
    'fields': [
        # {'items': ['NBA'], 'target': 'hashtag'}
        # {'items': ['TourdeFrance'], 'target': 'hashtag'}
        # {'items': ['UEFANationsLeague'], 'target': 'hashtag'}
        # {'items': ['csgo'], 'target': 'hashtag'}
        # {'items': ['leagueoflegends'], 'target': 'hashtag'}
        # {'items': ['dota2'], 'target': 'hashtag'}

    ],
    'since': '2021-09-01',
    'until': '2021-12-18'
}
f = open("../data/lolworld.txt", "a+")
for tweet in BlueBird().search(query):
    print(tweet)
    f.write(json.dumps(tweet))