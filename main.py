from superhero.superhero_api import SuperHero
import pandas as pd
from pprint import pprint

heroes_names = ('Hulk', 'Captain America', 'Thanos')
power_stats_compare_param = 'intelligence'


def best_hero_by_power_stats(compare_param, hero_names=None):
    """Сравнение нескольких заданных (или всех) героев по любому доступному показателю из категории 'powerstats'"""

    search_column = 'powerstats'

    super_hero = SuperHero()
    heroes = super_hero.get_all_heroes()

    # Для ускорения поиска информации по полученным 'json' данным, создаем структуру данных 'pandas DataFrame'
    all_heroes_df = pd.DataFrame(heroes)

    # Получаем список индексов строк (выборку) нужных нам героев в таблице pandas (не путать с показателем 'id' героя !!!)
    hero_indexes_for_search = all_heroes_df[all_heroes_df['name'].isin(heroes_names)].index if hero_names \
        else range(all_heroes_df.shape[0])
    # Создаем новую структуру данных (словарь) с нужными нам данными героев {id: powerstats} для их сравнения
    # TODO 1: в принципе, можно не создавать новую структуру данных 'heroes_power_stats', а работать с
    #  уже имеющимся у нас pandas датафреймом 'all_heroes_df', но для этого нужно немного заморочиться
    #  и распаковать вложенные составные 'json' данные 'powerstats' в отдельные колонки уже имеющегося датафрейма.
    #  Попробую реализовать это позднее :)
    heroes_power_stats = {all_heroes_df.loc[hero_ind, 'id']: heroes[hero_ind].get(search_column)
                          for hero_ind in hero_indexes_for_search}
    print(f'Супергерои для сравнения по показателю "{compare_param}" в формате {{id: {{powerstats}}}}:')
    pprint(heroes_power_stats)

    # Находим лучшего супергероя из сформированной ранее выборки
    if len(heroes_power_stats) > 0 and compare_param in list(heroes_power_stats.values())[0]:
        best_hero_id = max(heroes_power_stats, key=lambda itm: heroes_power_stats[itm].get(compare_param))
        return best_hero_id, all_heroes_df[all_heroes_df['id'] == best_hero_id]['name'].values[0], heroes_power_stats[best_hero_id][compare_param]


if __name__ == '__main__':
    try:
        h_id, hero_name, param = best_hero_by_power_stats(power_stats_compare_param, hero_names=heroes_names)
        print(f'Лучший по показателю "{power_stats_compare_param}": {hero_name}, '
              f'id = {h_id}, {power_stats_compare_param} = {param}')
    except TypeError:
        print(f'Показатель "{power_stats_compare_param}" не найден! Пожалуйста, проверьте название показателя.')
