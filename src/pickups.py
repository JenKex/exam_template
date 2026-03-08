import random

# Divide away from 'item' and into 'Fruit', 'Trap' etc.
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

class Fruit(Item):
    def __init__(self, name, value=20, symbol="?"):
        super().__init__(name, value, symbol)

# Trap kanske borde vara en separat super-klass, eftersom den inte är en sak man kan plocka upp.

class Trap(Item):
    def __init__(self, name, value=-10, symbol="#"):
        super().__init__(name, value, symbol)

class Key(Item):
    def __init__(self, name, value=0, symbol="F"):
        super().__init__(name, value, symbol)

class Shovel(Item):
    def __init__(self, name, value=0, symbol="|"):
        super().__init__(name, value, symbol)

class Chest(Item):
    def __init__(self, name, value=0, symbol="O"):
        super().__init__(name, value, symbol)

pickups = [Item("carrot"), Fruit("apple"), Fruit("strawberry"), Fruit("cherry"), Fruit("watermelon"), Item("radish"), Item("cucumber"), Item("meatball"), Trap("bomb"), Trap("trap door"), Key("skeleton key"), Shovel("shovel")]
goodies = [item for item in pickups if not isinstance(item, (Trap, Key, Shovel))]

# def get_random_xy(grid):
#     x = grid.get_random_x()
#     y = grid.get_random_y()
#     return x, y

def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

def spawn_random_goodie(grid):
    # TODO: Check if there's an easier way to spawn a random instance of a class or subclass, possibly create new subclasses for non-fruit foods
    # actually should probably just copy the list while splitting out the traps
    random_index = random.randint(0, len(goodies))
    spawn_item = goodies[random_index]
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, spawn_item)
            break

def spawn_chests(grid):
    for item in pickups:
        if isinstance(item, Key):
            while True:
                x = grid.get_random_x()
                y = grid.get_random_y()
                if grid.is_empty(x, y):
                    grid.set(x, y, Chest("treasure chest"))
                    break