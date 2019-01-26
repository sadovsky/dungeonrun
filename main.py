import tdl
import colors


def init():
    tdl.set_font('assets/arial10x10.png', greyscale=True, altLayout=True)
    console = tdl.init(80, 50, title="Dungeon Run", fullscreen=False)
    tdl.set_fps(30)
    return console


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

def gameloop(console):
    while not tdl.event.is_window_closed():
        console.draw_char(playerx, playery, '@', bg=None, fg=colors.red)
        tdl.flush()
        console.draw_char(playerx, playery, ' ', bg=None, fg=colors.red)
        escape_pushed = handle_keys()
        if escape_pushed:
                break

playerx,playery=0,0
console = init()
gameloop(console)