import requests


class SuperHero:
    base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/'

    def get_all_heroes(self):
        get_all_url = self.base_url + 'all.json'
        resp = requests.get(get_all_url)
        return resp.json()

    def get_hero_power_stats_by_id(self, hero_id):
        get_id_url = self.base_url + 'powerstats/' + str(hero_id) + '.json'
        return requests.get(get_id_url).json()
