from items.item import Item


class VoidStaff(Item):
    def __init__(self):
        super().__init__()
        self.cost = 2800
        self.type = 'legendary'
        self.ap = 65
        self.magic_pen_percentage = 0.4


class ShadowFlame(Item):
    def __init__(self):
        super().__init__()
        self.cost = 3000
        self.type = 'legendary'
        self.ap = 100
        self.hp = 200
        self.magic_pen_flat = 10

    def update_stats(self, character, enemy_character):
        if enemy_character.shielded or enemy_character._stats.hp.value < 1000:
            self.magic_pen_flat = 20
        return


class Zhonya(Item):
    def __init__(self):
        super().__init__()
        self.cost = 2600
        self.type = 'legendary'
        self.ap = 65
        self.armor = 45
        self.ability_haste = 10


class Rabadon(Item):
    def __init__(self):
        super().__init__()
        self.cost = 3600
        self.type = 'legendary'
        self.calculation_priority = 1
        self._ap = 120
        self.ap = 120

    def character_update(self, character):
        self.ap = self._ap + character._stats.ap._value * 0.35
        return


class Rylai(Item):
    def __init__(self):
        super().__init__()
        self.cost = 2800
        self.type = 'legendary'
        self.ap = 75
        self.hp = 400

    def update_stats(self, character, enemy_character):
        enemy_character._stats.ms = enemy_character._stats._ms * 0.4
        return
