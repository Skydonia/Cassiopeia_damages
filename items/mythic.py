from items.item import Item
from spells.item_spells import *

class Luden(Item):
    def __init__(self):
        super().__init__()
        self.cost = 3200
        self.type = 'mythic'
        self.ap = 80
        self._magic_pen_flat = 6
        self.magic_pen_flat = 6
        self.mana = 600
        self.ability_haste = 20
        self.spells = [Echo()]
        # self._damage = 100
        # self.damage = 100

    # def calculate_echo_damage(self, character):
    #     self.damage = self._damage + 0.1 * character._stats.ap.value
    #     return

    def calculate_mythic_passive(self, character):
        self.magic_pen_flat = self._magic_pen_flat + 5 * len([item for item in character.items if item.type == 'legendary'])
        return

    def character_update(self, character):
        self.calculate_mythic_passive(character)
        # self.calculate_echo_damage(character)
        return


class Lyandri(Item):
    def __init__(self):
        super().__init__()
        self.cost = 3200
        self.type = 'mythic'
        self.ap = 80
        self.mana = 600
        self._ability_haste = 20
        self.ability_haste = 20
        self.spells = [Agony(), Torment()]
        # self._damage = 0
        # self.damage = 0
        # self._dot = 15
        # self.dot = 15
        # self.dot_time = 4

    # def update_stats(self, character, enemy_character):
    #     self.calculate_agony_damage(character, enemy_character)
    #     self.calculate_torment_damage(character, enemy_character)
    #     return
    #
    # def calculate_agony_damage(self, character, enemy_character):
    #     if enemy_character._stats.hp.bonus > 1250:
    #         self.damage = 0.12 * character._stats.damage.value
    #         return
    #     self.damage = self._damage
    #     return
    #
    # def calculate_torment_damage(self, character, enemy_character):
    #     self.dot = self._dot + 0.015 * character._stats.ap.value + 0.01 * enemy_character._stats.hp.value
    #     return

    def character_update(self, character):
        self.ability_haste = self._ability_haste + 5 * len([item for item in character.items if item.type == 'legendary'])
        return