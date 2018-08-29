import tcod as libtcod


class TileRenderer:
    def __init__(self, color, char):
        self.color = color
        self.char = char

    def render(self, console, x, y):
        libtcod.console_set_char_background(console, x, y, self.color, libtcod.BKGND_SET)
        libtcod.console_put_char(console, x, y, self.char)


class NullRenderer:
    def render(self, console, x, y):
        pass