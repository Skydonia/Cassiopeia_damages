from items.item import Item

class MockItem(Item):
    def __init__(self):
        super().__init__()
        self.cost = 0
        self.type = 'mock'
        self.hp = 2000