import warnings


class Spell():
    def __init__(self):
        self.name = self.__class__.__name__
        self.lvl = 0
        self.damage_table = {
            1: {'direct': 0, 'ap_percentage': 0, 'mana_cost': 0},
            2: {'direct': 0, 'ap_percentage': 0, 'mana_cost': 0},
            3: {'direct': 0, 'ap_percentage': 0, 'mana_cost': 0},
            4: {'direct': 0, 'ap_percentage': 0, 'mana_cost': 0},
            5: {'direct': 0, 'ap_percentage': 0, 'mana_cost': 0}
        }
        self.cooldown = 0
        self.available = True

    def mitigation(self, true_damage):
        if self.effective_mr > 0:
            return true_damage * (100 / (100 + self.effective_mr))
        return true_damage * (2 - (100 / (100 - self.effective_mr)))

    def penetration_percentage(self, character):
        self.effective_mr *= (1-character.stats.magic_pen_percentage.value)
        if self.effective_mr < 0:
            self.effective_mr = 0
        return

    def penetration_flat(self, character, target):
        self.effective_mr = target.stats.magic_resist.value - character.stats.magic_pen_flat.value
        return self.effective_mr

    def true_damage(self, character):
        if self.lvl == 0:
            warnings.warn('spell not learned')
            return 0
        return self.damage_table[self.lvl]['direct'] + self.damage_table[self.lvl]['ap_percentage'] * character.stats.ap.value

    def hit(self, target, source):
        if self.lvl == 0 or not self.available:
            return 0
        self.penetration_flat(source, target)
        self.penetration_percentage(source)
        return self.mitigation(self.true_damage(source))
