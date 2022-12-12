import requests

file_list = ['1.txt', '2.txt', '3.txt']

class YaUploader:

    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json/txt', 'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self, disk_file_name):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/{disk_file_name}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, local_file_name, disk_file_name):
        upload_link = self.get_upload_link(disk_file_name)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(local_file_name, 'rb'))
        if response.status_code == 201:
            print('Загрузка прошла успешно')

    def multiple_upload(self, file_list):
        for file in file_list:
            disk_file_name = file
            local_file_name = file
            upload_link = self.get_upload_link(disk_file_name)
            response = requests.put(upload_link, headers=self.get_headers(), data=open(local_file_name, 'rb'))
            if response.status_code == 201:
                print(f'Загрузка файла {file} прошла успешно')


uploader = YaUploader("Указать свой токен")
# uploader.upload('2.txt', '2.txt')
# uploader.multiple_upload(file_list)
