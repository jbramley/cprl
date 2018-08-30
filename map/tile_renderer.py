import tcod as libtcod


class TileRenderer:
    def __init__(self, fov_color, hidden_color):
        self.fov_color = fov_color
        self.hidden_color = hidden_color
        self.tile = None

    def render(self, console, fov_map, x, y):
        if libtcod.map_is_in_fov(fov_map, x, y):
            color = self.fov_color
            self.tile.explored = True
        else:
            if self.tile.explored:
                color = self.hidden_color
            else:
                return
        libtcod.console_set_char_background(console, x, y, color, libtcod.BKGND_SET)


class NullRenderer:
    def render(self, console, fov_map, x, y):
        pass