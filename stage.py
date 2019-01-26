class Tile:
    # a tile of the map and its properties
    def __init__(self, blocking):
        self.blocking = blocking


class Stage:

    def __init__(self, width, height):
        self.map = [[Tile(False) for y in range(height)] for x in range(width)]
