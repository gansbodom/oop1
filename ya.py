import os
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        self.file_path = file_path
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resourses/upload'
        headers = {'Content-Type': 'application/json', 'Autorization': f'OAuth {self.token}'}
        params = {"path": f"{self.file_path}"}
        r = requests.get(upload_url, headers=headers, params=params)
        print(r.json())
        href = r.json()["href"]
        requests.put(href, data=open(self.file_path, 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.abspath('/home/bn/python/PycharmProjects/oop1/test.txt')
    uploader = YaUploader('y0_AgAAAABR2QGiAADLWwAAAADjyvy_4jNywNthRsO5PHTsIPOSpToCxrw')
    result = uploader.upload(path_to_file)