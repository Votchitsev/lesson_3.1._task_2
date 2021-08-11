import os
import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_list = os.listdir(file_path)
        API_BASE_URL = 'https://cloud-api.yandex.net/'
        print(file_list)
        for file in file_list:
            file_directory = 'HW_3.1./' + file
            params_get = {'path': file_directory}
            headers = {'authorization': f'OAuth {token}',
                       'accept': 'application/json'}
            r = requests.get(API_BASE_URL + 'v1/disk/resources/upload', params=params_get, headers=headers)
            pprint(r.json())
            with open(file_path + file, 'rb') as f:
                upload_file = requests.put(r.json()['href'], headers=headers, data=f)
                pprint(upload_file)


if __name__ == '__main__':
    path_to_file = '/home/dmitry/PycharmProjects/HW_lesson_3.1._task_2/Upload/'
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


