import requests

heroes_lst = ['Hulk', 'Captain America', 'Thanos']
heroes_dct = {}

headers = {'Content-Type': 'text/html', 'charset': 'utf-8'}
responce = requests.get('https://akabab.github.io/superhero-api/api/all.json', headers=headers)


for i in responce.json():
    if i['name'] in heroes_lst:
        heroes_dct[i['powerstats']['intelligence']] = i['name']

print(heroes_dct[max(heroes_dct.keys())])
