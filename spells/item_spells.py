from .spell import Spell

class Echo(Spell):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.damage_table = {
            0: {'direct': 100, 'ap_percentage': 0.1, 'mana_cost': 0, 'cooldown': 10}
        }
        self.available =True

    def true_damage(self, character):
        return self.damage_table[self.lvl]['direct'] + self.damage_table[self.lvl][
            'ap_percentage'] * character.stats.ap.value

    def hit(self, target, source):
        if self.available:
            self.available = False
            self.penetration_flat(source, target)
            self.penetration_percentage(source)
            return self.mitigation(self.true_damage(source))
        return 0

class Agony(Spell):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__

    def hit(self, target, source):
        self.penetration_flat(source, target)
        self.penetration_percentage(source)
        if target.stats.hp.bonus > 1250:
            return self.mitigation(0.12 * source.stats.damage.current_value)
        return 0

class Torment(Spell):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.damage_table = {
            0: {'direct': 15, 'ap_percentage': 0.015, 'mana_cost': 0}
        }

    def true_damage(self, character):
        return self.damage_table[self.lvl]['direct'] + self.damage_table[self.lvl]['ap_percentage'] * character.stats.ap.value

    def hit(self, target, source):
        self.penetration_flat(source, target)
        self.penetration_percentage(source)
        return self.mitigation(self.true_damage(source) + 0.01 * target.stats.hp.value)