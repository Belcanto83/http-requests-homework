import requests


class SuperHero:
    base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/'

    def get_all_heroes(self):
        """Получить через API сайта список всех супергероев в формате 'json'"""

        get_all_url = self.base_url + 'all.json'
        resp = requests.get(get_all_url)
        return resp.json()
