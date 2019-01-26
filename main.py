import tdl
import colors
import window
import object

def handle_keys(hero):
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
        hero.y -= 1

    elif user_input.key == 'DOWN':
        hero.y += 1

    elif user_input.key == 'LEFT':
        hero.x -= 1

    elif user_input.key == 'RIGHT':
        hero.x += 1

def gameloop(w):
    hero = object.GameObject(1, 1, '@', colors.red)
    npc = object.GameObject(20, 20, 'X', colors.blue)
    objects = [hero, npc]

    while not tdl.event.is_window_closed():
        for obj in objects:
            obj.draw(w.con)

        w.root.blit(w.con, 0, 0, w.screen.width, w.screen.height, 0, 0)
        tdl.flush()

        for obj in objects:
            obj.clear(w.con)

        escape_pushed = handle_keys(hero)
        if escape_pushed:
                break

w = window.Window()
gameloop(w)