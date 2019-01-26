import tdl
import colors


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Window:
    screen = Screen(80,50)

    def __init__(self):
        tdl.set_font('assets/arial10x10.png', greyscale=True, altLayout=True)
        self.root = tdl.init(self.screen.width, self.screen.height, title="Dungeon Run", fullscreen=False)
        self.con = tdl.Console(self.screen.width, self.screen.height)
        tdl.set_fps(30)

def handle_keys():
    global playerx, playery
    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
           user_input = event
           keypress = True
    if not keypress:
        return

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen())

    elif user_input.key == 'ESCAPE':
        return True  # exit game

    # movement keys
    if user_input.key == 'UP':
        playery -= 1

    elif user_input.key == 'DOWN':
        playery += 1

    elif user_input.key == 'LEFT':
        playerx -= 1

    elif user_input.key == 'RIGHT':
        playerx += 1

def gameloop(w):
    while not tdl.event.is_window_closed():
        w.con.draw_char(playerx, playery, '@', bg=None, fg=colors.red)
        w.root.blit(w.con, 0, 0, w.screen.width, w.screen.height, 0, 0)
        tdl.flush()
        w.con.draw_char(playerx, playery, ' ', bg=None, fg=colors.red)
        escape_pushed = handle_keys()
        if escape_pushed:
                break

playerx,playery=0,0
w = Window()
gameloop(w)