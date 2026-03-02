from .grid import Grid
from .player import Player
from . import pickups



player = Player(int(Grid.width / 2), int(Grid.height / 2))
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"

# Originally wanted to have item_check be a function and a part of move_player, but updating global variables in functions is considered bad practice.
# def item_check(score):
    # maybe_item = g.get(player.pos_x, player.pos_y)
    # if isinstance(maybe_item, pickups.Item):
    #     # we found something
    #     print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
    #     score += maybe_item.value
    #     #g.set(player.pos_x, player.pos_y, g.empty)
    #     g.clear(player.pos_x, player.pos_y)

def clear_space():
     g.clear(player.pos_x, player.pos_y)

def move_player(command):
    if (command == 'a') and player.can_move(-1, 0, g):
        player.move(-1, 0)
    elif (command == 'd') and player.can_move(1, 0, g):
        player.move(1, 0)
    elif (command == 'w') and player.can_move(0, -1, g):
        player.move(0, -1)
    elif (command == 's') and player.can_move(0, 1, g):
        player.move(0, 1)

def took_step(prev_player_pos_x, prev_player_pos_y):
    if prev_player_pos_x != player.pos_x or prev_player_pos_y != player.pos_y:
        return True
    else:
        return False

# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    prev_player_pos_x = player.pos_x
    prev_player_pos_y = player.pos_y
    move_player(command)
    maybe_item = g.get(player.pos_x, player.pos_y)
    if isinstance(maybe_item, pickups.Item):
        # we found something
        print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
        score += maybe_item.value
        g.clear(player.pos_x, player.pos_y)
    if took_step(prev_player_pos_x, prev_player_pos_y):
        score -= 1


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
