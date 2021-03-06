
class GameObject:
    """
    Generic object: NPC, player, item, etc
    """

    def __init__(self, x, y, char, color):
        """
        :param char: Character to represent object, ie "sprite"
        """
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy, stage):
        # move by the given amount
        if not stage.map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self, con):
        # draw the character that represents this object at its position
        con.draw_char(self.x, self.y, self.char, self.color)

    def clear(self, con):
        # erase the character that represents this object
        con.draw_char(self.x, self.y, ' ', self.color, bg=None)
