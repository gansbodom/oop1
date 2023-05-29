# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         """Метод загружает файлы по списку file_list на яндекс диск"""
#         # Тут ваша логика
#         # Функция может ничего не возвращать
#
#
# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     path_to_file = ...
#     token = ...
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)
#
#
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    # def get_headers(self):
    #     return {
    #         'Content-Type': 'application/json',
    #         'Autorization': f'OAuth {self.token}'
    #     }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # upload_url = "https://cloud-api.yandex.net/v1/disk/resourses/upload"
        # headers = self.get_headers()
        # responce = requests.put(url="https://cloud-api.yandex.net/, data="./test.txt")
        # Тут ваша логика
        # Функция может ничего не возвращать
        self.file_path = file_path
        headers = {'Content-Type': 'application/json', 'Autorization': f'OAuth {self.token}'}
        params = {"path": "Тест API"}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resourses/upload"
        href = requests.get(upload_url, headers=headers)
        responce = requests.put(href, data=open(file_path, 'rb'))

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = 'y0_AgAAAABR2QGiAADLWwAAAADjyvy_4jNywNthRsO5PHTsIPOSpToCxrw'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)