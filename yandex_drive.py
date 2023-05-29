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
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Content-Type": "application/json", "Authorization": self.token}
        params = {"path": f"test/{path_to_file}"}
        r = requests.get(upload_url, headers=headers, params=params)
        href = r.json()["href"]
        requests.put(href, data=open(self.file_path, 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    uploader = YaUploader('y0_AgAAAABR2QGiAADLWwAAAADjyvy_4jNywNthRsO5PHTsIPOSpToCxrw')
    uploader.upload(os.path.abspath(path_to_file))
