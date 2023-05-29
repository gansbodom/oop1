# import requests
# import pprint
#
# class YandexDisk:
#
#
#
#     def __init__(self, token):
#         self.token = token
#         self.yandex_url = 'https://cloud-api.yandex.net'
#
#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json'
#             'Autorization': f'OAuth {self.token}'
#         }
#
#     def get_file_list(self):
#         files_url = f'{self.yandex_url}/v1/disk/resourses/files/'
#         headers = self.get_headers()
#         response = requests.get(files_url, headers=headers)
#         return response.json()
#
#     def get_upload_link(self, disk_file_path):
#         upload_url = "http://cloud-api.yandex.net/v1/disk/resourses/upload"
#         headers = self.get_headers()
#         params = {"path" : disk_file_path, "overwrite":"true"}
# #token = y0_AgAAAABR2QGiAADLWwAAAADjyvy_4jNywNthRsO5PHTsIPOSpToCxrw
# ya = YandexDisk(token="")
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
        self.token = 'y0_AgAAAABR2QGiAADLWwAAAADjyvy_4jNywNthRsO5PHTsIPOSpToCxrw'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Autorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resourses/upload"
        headers = self.get_headers()
        responce = requests.put(url="https://cloud-api.yandex.net/, data="./test.txt")

        # Тут ваша логика
        # Функция может ничего не возвращать

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)