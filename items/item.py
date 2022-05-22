import inspect
import operator

class Item:
    def __init__(self):
        self.name = self.__class__.__name__
        self.cost = None
        self.type = 'legendary'
        self.calculation_priority = 0

    def _pattern(self, other, my_operator):
        return my_operator(self.calculation_priority, other.calculation_priority)

    def __lt__(self, other):
        ops = inspect.currentframe().f_code.co_name
        return self._pattern(other, getattr(operator, ops.replace('_', '')))

    def __gt__(self, other):
        ops = inspect.currentframe().f_code.co_name
        return self._pattern(other, getattr(operator, ops.replace('_', '')))

    def __le__(self, other):
        ops = inspect.currentframe().f_code.co_name
        return self._pattern(other, getattr(operator, ops.replace('_', '')))

    def __ge__(self, other):
        ops = inspect.currentframe().f_code.co_name
        return self._pattern(other, getattr(operator, ops.replace('_', '')))

    def character_update(self, character):
        return

    def update_stats(self, character, enemy_character):
        return