from .spell import Spell
import warnings


class NoxiousBlast(Spell):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.damage_table = {
            1: {'direct': 75, 'ap_percentage': 0.9, 'mana_cost': 50, 'cooldown': 3.5},
            2: {'direct': 110, 'ap_percentage': 0.9, 'mana_cost': 55, 'cooldown': 3.5},
            3: {'direct': 145, 'ap_percentage': 0.9, 'mana_cost': 60, 'cooldown': 3.5},
            4: {'direct': 180, 'ap_percentage': 0.9, 'mana_cost': 65, 'cooldown': 3.5},
            5: {'direct': 215, 'ap_percentage': 0.9, 'mana_cost': 70, 'cooldown': 3.5}
        }


class Miasma(Spell):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.damage_table = {
            1: {'direct': 20, 'ap_percentage': 0.15, 'mana_cost': 70, 'cooldown': 24},
            2: {'direct': 25, 'ap_percentage': 0.15, 'mana_cost': 80, 'cooldown': 22},
            3: {'direct': 30, 'ap_percentage': 0.15, 'mana_cost': 90, 'cooldown': 20},
            4: {'direct': 35, 'ap_percentage': 0.15, 'mana_cost': 100, 'cooldown': 18},
            5: {'direct': 40, 'ap_percentage': 0.15, 'mana_cost': 110, 'cooldown': 16}
        }


class TwinFang(Spell):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.damage_table = {
            1: {'direct': 20, 'ap_percentage': 0.6, 'mana_cost': 50, 'cooldown': 0.75},
            2: {'direct': 40, 'ap_percentage': 0.6, 'mana_cost': 48, 'cooldown': 0.75},
            3: {'direct': 60, 'ap_percentage': 0.6, 'mana_cost': 46, 'cooldown': 0.75},
            4: {'direct': 80, 'ap_percentage': 0.6, 'mana_cost': 44, 'cooldown': 0.75},
            5: {'direct': 100, 'ap_percentage': 0.6, 'mana_cost': 42, 'cooldown': 0.75}
        }

    def true_damage(self, character):
        if self.lvl == 0:
            warnings.warn('spell not learned')
            return 0
        return 48 + 4 * character.lvl + 0.1 * character.stats.ap.value + \
               self.damage_table[self.lvl]['direct'] + self.damage_table[self.lvl]['ap_percentage'] * character.stats.ap.value


class PetrifyingGaze(Spell):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.damage_table = {
            1: {'direct': 150, 'ap_percentage': 0.5, 'mana_cost': 100, 'cooldown': 120},
            2: {'direct': 250, 'ap_percentage': 0.5, 'mana_cost': 100, 'cooldown': 100},
            3: {'direct': 350, 'ap_percentage': 0.5, 'mana_cost': 100, 'cooldown': 80}
        }
