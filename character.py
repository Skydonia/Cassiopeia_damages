from stats.stat import *
from items import *
from stats.stats import Stats
from spells.cassiopeia_spells import *

class Character():
    def __init__(self):
        self.name = self.__class__.__name__
        self.lvl = 1
        self.shielded = False
        self.spells = {}
        self.items = [MockItem()]
        self._stats = Stats(
            ap=ap(0),
            hp=hp(500, 0),
            mana=mana(100, 0),
            ms=ms(300, 0),
            armor=armor(0, 0),
            magic_resist=magic_resist(0, 0)
        )
        self.target = None

    def __getitem__(self, arg):
        possibilities = [getattr(self._stats,stat) for stat in self._stats.__dict__ if stat == arg]
        possibilities += [self.spells[spell] for spell in self.spells if spell == arg.upper()]
        if len(possibilities) == 0:
            return None
        if len(possibilities) == 1:
            return possibilities[0]
        return possibilities

    @property
    def stats(self):
        if self.target is None:
            self.target = Character()
        self._stats.update(self, self.target)
        return self._stats

    @property
    def alive(self):
        if self.stats.hp.value > 0:
            return True
        return False


class Cassiopeia(Character):
    def __init__(self):
        super().__init__()
        self.lvl = 18
        self._stats = Stats(
            ap=ap(0),
            hp=hp(560, 90),
            mana=mana(350, 60),
            ms=ms(328, 4),
            armor=armor(0, 0),
            magic_resist=magic_resist(0, 0)
        )
        self.spells = {
            'Q': NoxiousBlast(),
            'Z': Miasma(),
            'E': TwinFang(),
            'R': PetrifyingGaze()
        }
        self.damage_historic = []

    def update_historic(self, spell, damages):
        self.damage_historic += [{spell.name:damages}]
        return

    def launch_item_spells(self, target):
        for item in self.items:
            if 'spells' in item.__dict__:
                for spell in item.spells:
                    self.hit_marker(spell, target)
        return

    def hit_marker(self, spell, target):
        damages = spell.hit(target=target, source=self)
        target.stats.hp -= damages
        self.update_historic(spell, damages)
        return damages

    def cast(self, spell, target):
        damages = self.hit_marker(spell, target)
        self.stats.damage.current_value = damages
        self.launch_item_spells(target)
        return
