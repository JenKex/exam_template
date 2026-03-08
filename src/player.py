class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        # TODO: clean up, possibly divide into function
        # next_step = self.pos_x + x, self.pos_y + y
        if grid.get(self.pos_x + x, self.pos_y + y) == grid.wall:
            print('False')
            return False
        else:
            return True
        #TODO: returnera True om det inte står något i vägen


