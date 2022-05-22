from character import Character, Cassiopeia
import pandas as pd
from items import *
from visualizer import Visualize


def simulation(sardoche, target_mr=0):
    manequin = Character()
    manequin['magic_resist'].base_value = target_mr
    sardoche.cast(sardoche['Q'], manequin)
    for _ in range(4):
        sardoche.cast(sardoche['E'], manequin)
    recap_dict = {'target_magic_rest': target_mr}
    total = 0
    for e in sardoche.damage_historic:
        for key in e:
            total += e[key]
            if key in recap_dict:
                recap_dict[key] += e[key]
                continue
            recap_dict[key] = e[key]
    recap_dict['total'] = total
    return recap_dict


def reset_sard(item_set):
    sardoche = Cassiopeia()
    sardoche.items = item_set
    sardoche['E'].lvl = 5
    sardoche['Q'].lvl = 5
    return sardoche

def simulate(item_name_list,overall_results=[],subplot_titles=[]):
    result_list = []
    for target_mr in range(0, 200):
        sardoche = reset_sard([globals()[item_name]() for item_name in item_name_list])
        result_list.append(simulation(sardoche, target_mr))
    results = pd.DataFrame(result_list)
    overall_results.append(results)
    title=''
    for item in item_name_list:
        title+=f'+{item}'
    title+=f" (total golds: {sum([item.cost for item in sardoche.items])})"
    subplot_titles.append(title[1:])
    return

if __name__ == '__main__':
    overall_results = []
    subplot_titles = []
    simulate(['Rabadon', 'ShadowFlame', 'Luden'], overall_results, subplot_titles)
    simulate(['Rabadon', 'ShadowFlame', 'Lyandri'], overall_results, subplot_titles)
    simulate(['Rabadon', 'VoidStaff', 'Luden'], overall_results, subplot_titles)
    simulate(['Rabadon', 'VoidStaff', 'Lyandri'], overall_results, subplot_titles)
    Visualize(overall_results, "./outputs/set_3_items.html", subplot_titles)

    overall_results = []
    subplot_titles = []
    simulate(['ShadowFlame', 'Lyandri'], overall_results, subplot_titles)
    simulate(['VoidStaff', 'Lyandri'], overall_results, subplot_titles)
    simulate(['Rabadon', 'Lyandri'], overall_results, subplot_titles)
    simulate(['Rabadon', 'Luden'], overall_results, subplot_titles)
    Visualize(overall_results, "./outputs/set_2_items.html", subplot_titles)

    print('done')
