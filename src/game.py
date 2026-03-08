from .grid import Grid
from .player import Player
from . import pickups



player = Player(int(Grid.width / 2), int(Grid.height / 2))
score = 0
step_count = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
g.make_straight_walls()
pickups.randomize(g)
pickups.spawn_chests(g)


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

# ändrade move_action till player_action, tar alla commands
def player_action(command):
    if (command == 'a') and player.can_move(-1, 0, g):
        player.move(-1, 0)
    elif (command == 'd') and player.can_move(1, 0, g):
        player.move(1, 0)
    elif (command == 'w') and player.can_move(0, -1, g):
        player.move(0, -1)
    elif (command == 's') and player.can_move(0, 1, g):
        player.move(0, 1)
    elif (command == 'i'):
        if len(inventory) == 0:
            print("You're not carrying anything. Try picking something up!")
        else:
            print('You currently have: ' + ', '.join(inventory))

def took_step(prev_player_pos_x, prev_player_pos_y):
    if prev_player_pos_x != player.pos_x or prev_player_pos_y != player.pos_y:
        return True
    else:
        return False

# should divide g.clear into a function

# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    prev_player_pos_x = player.pos_x
    prev_player_pos_y = player.pos_y
    player_action(command)
    maybe_item = g.get(player.pos_x, player.pos_y)
    if isinstance(maybe_item, pickups.Item):
        if isinstance(maybe_item, pickups.Trap):
            print(f"Oh no! A {maybe_item.name}!")
            score += maybe_item.value
        elif isinstance(maybe_item, pickups.Key) or isinstance(maybe_item, pickups.Shovel):
            print(f"You found a {maybe_item.name}. It might come in handy!")
            inventory.append(maybe_item.name)
            g.clear(player.pos_x, player.pos_y)
        elif isinstance(maybe_item, pickups.Chest):
            # really want to check for keys with a class check, but isinstance would require a for-loop checking every item, which feels inefficient
                #for item in inventory:    
                # if isinstance(item, pickups.Key):
                #     print(f"You opened the {maybe_item.name}. Inside was a bar of gold!")
                #     score +=100
                # else:
                #     print(f"You can't open the {maybe_item.name}. Maybe you need a key...")
            # otherwise:
            if "skeleton key" in inventory:
                print(f"You opened the {maybe_item.name}. Inside was a bar of gold!")
                score +=100
                inventory.remove("skeleton key")
                g.clear(player.pos_x, player.pos_y)
            else:
                print(f"You can't open the {maybe_item.name}. Maybe you need a key...")
        else:
        # we found something
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            score += maybe_item.value
            inventory.append(maybe_item.name)
            g.clear(player.pos_x, player.pos_y)
    if took_step(prev_player_pos_x, prev_player_pos_y):
        score -= 1
        step_count += 1
    if step_count % 25 == 0:
        pickups.spawn_random_goodie(g)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
