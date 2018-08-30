import tcod as libtcod
from input import handle_keys
from entity import Entity
from fov import initialize_fov, recompute_fov
from render import render_all, clear_all
from map.game_map import GameMap


def main():
    screen_width = 80
    screen_height = 50

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'Cyberpunk Roguelike', False)

    con = libtcod.console_new(screen_width, screen_height)

    game_map = GameMap(5, 4)
    player_start = game_map.starting_point()
    player = Entity(player_start[0], player_start[1], '@', libtcod.white)
    npc = Entity(player_start[0] + 2, player_start[1] + 2, '@', libtcod.yellow)
    entities = [npc, player]

    fov_recompute = True
    fov_map = initialize_fov(game_map)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height)
        fov_recompute = False

        libtcod.console_flush()

        clear_all(con, entities)

        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
                fov_recompute = True

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()