import tdl
import colors

def init():
    tdl.set_font('assets/arial10x10.png', greyscale=True, altLayout=True)
    console = tdl.init(80, 50, title="Dungeon Run", fullscreen=False)
    tdl.setFPS(30)
    return console

def key_event():
    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
            user_input = event
            keypress = True
    if not keypress:
        return
    else:
        return user_input.key


def gameloop(console):
    while not tdl.event.is_window_closed():
        console.draw_char(20, 20, '@', bg=None, fg=colors.red)
        tdl.flush()
        user_input = key_event()
        if user_input:
            if user_input.key == 'ESCAPE':
                break

console = init()
gameloop(console)