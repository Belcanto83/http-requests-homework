from superhero.superhero_api import SuperHero
import pandas as pd
from pprint import pprint

heroes_names = ('Hulk', 'Captain America', 'Thanos')
power_stats_compare_param = 'intelligence'


def best_hero_by_power_stats(hero_names, compare_param):
    def get_id_by_name(name, all_heroes_df):
        hero = all_heroes_df[all_heroes_df['name'] == name]
        try:
            res = int(hero['id'])
        except TypeError:
            res = -1
        return res

    super_hero = SuperHero()
    heroes = super_hero.get_all_heroes()
    all_heroes = pd.DataFrame(heroes)
    heroes_ids = {name: get_id_by_name(name, all_heroes) for name in hero_names}
    pprint(heroes_ids)
    heroes_power_stats = {hero_id: super_hero.get_hero_power_stats_by_id(hero_id)
                          for hero_id in heroes_ids.values() if hero_id > 0}
    pprint(heroes_power_stats)
    if len(heroes_power_stats) > 0 and compare_param in list(heroes_power_stats.values())[0]:
        best_hero_id = max(heroes_power_stats, key=lambda itm: heroes_power_stats[itm].get(compare_param))
        return best_hero_id, all_heroes[all_heroes['id'] == best_hero_id]['name'].values[0], heroes_power_stats[best_hero_id][compare_param]


if __name__ == '__main__':
    try:
        h_id, hero_name, param = best_hero_by_power_stats(heroes_names, power_stats_compare_param)
        print(f'Лучший по показателю "{power_stats_compare_param}": {hero_name}, '
              f'id = {h_id}, {power_stats_compare_param} = {param}')
    except TypeError:
        print(f'Показатель "{power_stats_compare_param}" не найден! Пожалуйста, проверьте название показателя.')
