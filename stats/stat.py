class Stat:
    def __init__(self, base_value, value_per_lvl=0):
        self.name = self.__class__.__name__
        self._current_items = []
        self._current_lvl = 1
        self.base_value = base_value
        self.value_per_lvl = value_per_lvl
        self.loss = 0
        self.current_value = self.value

    def __isub__(self, value):
        self.loss += value
        return self

    def __iadd__(self, value):
        self.loss -= value
        return self

    @property
    def _value(self):
        base_value = self.base
        for item in self._current_items:
            if '_' + self.name in item.__dict__:
                base_value += getattr(item, '_' + self.name)
            else:
                if self.name in item.__dict__:
                    base_value += getattr(item, self.name)
        return base_value

    @property
    def bonus(self):
        return self.value - self.base

    @property
    def value(self):
        base_value = self.base
        for item in self._current_items:
            if self.name in item.__dict__:
                base_value += getattr(item, self.name)
        return base_value - self.loss

    @property
    def base(self):
        return self.base_value + self.value_per_lvl * self._current_lvl

    def update(self, character, enemy_character):
        self._current_lvl = character.lvl
        self._current_items = character.items
        self._current_items.sort()
        self._current_items =self._current_items [::-1]
        for item in self._current_items:
            item.character_update(character)
            item.update_stats(character, enemy_character)
        return

class hp(Stat):
    def __init__(self, base_value, value_per_lvl):
        super().__init__(base_value, value_per_lvl)

class mana(Stat):
    def __init__(self, base_value, value_per_lvl):
        super().__init__(base_value, value_per_lvl)

class ap(Stat):
    def __init__(self, base_value):
        super().__init__(base_value)

class ms(Stat):
    def __init__(self, base_value, value_per_lvl):
        super().__init__(base_value, value_per_lvl)

class armor(Stat):
    def __init__(self, base_value, value_per_lvl):
        super().__init__(base_value, value_per_lvl)

class magic_resist(Stat):
    def __init__(self, base_value, value_per_lvl):
        super().__init__(base_value, value_per_lvl)

class ability_haste(Stat):
    def __init__(self, base_value, value_per_lvl):
        super().__init__(base_value, value_per_lvl)

class damage(Stat):
    def __init__(self, base_value=0):
        super().__init__(base_value)

class dot(Stat):
    def __init__(self, base_value=0):
        super().__init__(base_value)

class magic_pen_flat(Stat):
    def __init__(self, base_value):
        super().__init__(base_value)

class magic_pen_percentage(Stat):
    def __init__(self, base_value):
        super().__init__(base_value)