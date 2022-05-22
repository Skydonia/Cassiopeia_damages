from .stat import *

class Stats:
    def __init__(self, **kwargs):
        self.ability_haste = ability_haste(0, 0)
        self.damage = damage()
        self.dot = dot()
        self.magic_pen_flat = magic_pen_flat(0)
        self.magic_pen_percentage = magic_pen_percentage(0)
        self.__dict__.update(**kwargs)

    def update(self, character, target):
        for stat in list(self.__dict__.keys()):
            getattr(self, stat).update(character, target)
        return