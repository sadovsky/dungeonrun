import tdl


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Window:
    screen = Screen(80, 50)

    def __init__(self):
        tdl.set_font('assets/arial10x10.png', greyscale=True, altLayout=True)
        self.root = tdl.init(self.screen.width, self.screen.height, title="Dungeon Run", fullscreen=False)
        self.con = tdl.Console(self.screen.width, self.screen.height)
        tdl.set_fps(30)
