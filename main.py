# This is a sample Python script.
import requests
import pandas as pd
import urllib.request


def import_card_data():
    r = requests.get('https://c2.scryfall.com/file/scryfall-bulk/default-cards/default-cards-20211001210244.json')
    dic = r.json()
    print(len(dic))
    return dic


def convert_to_DataFrame(dic):
    #for x in dic:print(str(x.keys()))
    df = pd.DataFrame(dic)
    print(df)
    print(df.keys())
    return dic


#    df = pd.read
fil = convert_to_DataFrame(import_card_data())
# print(fil)
