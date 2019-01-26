import tdl
import colors
import window
import object
import stage

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
    npc = object.GameObject(10, 10, 'X', colors.blue, True)
    objects = [hero, npc]

    sta = stage.Stage(w.screen.width, w.screen.height)
    sta.map[5][5].blocking = True
    sta.map[15][15].blocking = True

    while not tdl.event.is_window_closed():
        for obj in objects:
            obj.draw(w.con)

        for x in range(w.screen.width):
            for y in range(w.screen.height):
                wall = sta.map[x][y].blocking
                if wall:
                    w.con.draw_char(x, y, None, fg=None, bg=colors.grey)
                else:
                    w.con.draw_char(x, y, None, fg=None, bg=colors.black)

        w.root.blit(w.con, 0, 0, w.screen.width, w.screen.height, 0, 0)
        tdl.flush()

        for obj in objects:
            obj.clear(w.con)

        escape_pushed = handle_keys(hero)
        if escape_pushed:
            break


w = window.Window()
gameloop(w)
