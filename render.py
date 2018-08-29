import tcod as libtcod


def render_all(con, entities, game_map, screen_width, screen_height, colors):
    for y in range(game_map.height):
        for x in range(game_map.width):
            game_map.tiles[x][y].renderer.render(con, x, y)
    for e in entities:
        draw_entity(con, e)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for e in entities:
        clear_entity(con, e)


def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)