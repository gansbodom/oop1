import os
import requests

file_path = os.path.abspath('test.txt')
upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
headers = {"Authorization": f"OAuth y0_AgAAAABR2QGiAADLWwAAAADjyvy_4jNywNthRsO5PHTsIPOSpToCxrw"}
params = {"path": "test/test.txt"}
r = requests.get(upload_url, params=params, headers=headers)
href = r.json()["href"]
print(r.json())
responce = requests.put(href, data=open(file_path))

