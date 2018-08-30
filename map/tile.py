import tcod as libtcod
from map.tile_renderer import TileRenderer, NullRenderer


class Tile:
    def __init__(self, renderer):
        self.blocked = False
        self.block_sight = False
        self.render = False
        self.explored = False
        self.renderer = renderer
        self.renderer.tile = self


class RoadTile(Tile):
    def __init__(self, renderer):
        super(RoadTile, self).__init__(renderer)
        self.blocked = False
        self.block_sight = False
        self.render = True


class NullTile(Tile):
    def __init__(self, renderer):
        super(NullTile, self).__init__(renderer)
        self.blocked = False
        self.block_sight = False
        self.render = False


class WallTile(Tile):
    def __init__(self, renderer):
        super(WallTile, self).__init__(renderer)
        self.blocked = True
        self.block_sight = True
        self.render = True


class TileFactory:
    NULL_TILE = 0
    ROAD_TILE = 1
    WALL_TILE = 2

    @staticmethod
    def create(typ):
        if typ == TileFactory.NULL_TILE:
            return NullTile(NullRenderer())
        elif typ == TileFactory.ROAD_TILE:
            return RoadTile(TileRenderer(libtcod.Color(50, 50, 150), libtcod.Color(200, 180, 50)))
        elif typ == TileFactory.WALL_TILE:
            return WallTile(TileRenderer(libtcod.Color(0, 0, 100), libtcod.Color(130, 110, 50)))
        else:
            return None


