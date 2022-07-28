import requests
from pprint import pprint


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self, params=None):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers, params=params)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def _get_download_link(self, disk_file_path):
        download_url = "https://cloud-api.yandex.net/v1/disk/resources/download"
        headers = self.get_headers()
        params = {"path": disk_file_path}
        response = requests.get(download_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        # response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def download_file_from_disk(self, disk_file_path, filename):
        href = self._get_download_link(disk_file_path=disk_file_path)
        headers = self.get_headers()
        response = requests.get(href['href'], headers=headers)
        with open(filename, 'wb') as file:
            file.write(response.content)
        response.raise_for_status()
        if response.status_code == 200:
            print("Success")
