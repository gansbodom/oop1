import requests

heroes_lst = ['Hulk', 'Captain America', 'Thanos']
heroes_dct = {}

responce = requests.get('https://akabab.github.io/superhero-api/api/all.json')

for i in responce.json():
    if i['name'] in heroes_lst:
        #print(i['name'], i['id'])
        heroes_dct[i['powerstats']['intelligence']] = i['name']

print(heroes_dct[max(heroes_dct.keys())])
