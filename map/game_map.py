from map.tile import NullTile, RoadTile, WallTile, Tile, TileFactory
from map.gridgraph import GridGraph
import random
from typing import List


class GameMap:
    def __init__(self, num_x_nodes, num_y_nodes, street_width=5, street_length=9, sparseness=0.7):
        self.street_width = street_width
        self.street_length = street_length
        self.sparseness = sparseness
        self.offset = street_width + street_length
        self.width = num_x_nodes * self.offset - street_length + 2
        self.height = num_y_nodes * self.offset - street_length + 2
        self.grid_graph = GridGraph(num_x_nodes, num_y_nodes)
        self.tiles = self.initialize_tiles()
        self.make_map()
        self.starting_node = None

    def initialize_tiles(self) -> List[List[Tile]]:
        tiles = [[TileFactory.create(TileFactory.NULL_TILE) for _ in range(self.height)] for _ in range(self.width)]
        return tiles

    def make_map(self):
        self.grid_graph.generate_map(self.sparseness)
        try:
            for n in self.grid_graph.nodes():
                self.add_intersection(n)
            for e in self.grid_graph.edges():
                if e[0][0] == e[1][0]:
                    self.add_vertical_road(e[0])
                else:
                    self.add_horizontal_road(e[0])
        except IndexError as err:
            print(err)

    def starting_point(self):
        if self.starting_node is None:
            self.starting_node = random.choice(self.grid_graph.nodes())
        return self.starting_node[0]*self.offset + 2 + 1, self.starting_node[1]*self.offset + 2 + 1

    def add_intersection(self, node):
        (w, h) = node
        for i in range(self.street_width + 2):
            self.tiles[self.offset * w + i][self.offset * h] = TileFactory.create(TileFactory.WALL_TILE)
            self.tiles[self.offset * w + i][self.offset * h + self.street_width + 1] = TileFactory.create(TileFactory.WALL_TILE)
            self.tiles[self.offset * w][self.offset * h + i] = TileFactory.create(TileFactory.WALL_TILE)
            self.tiles[self.offset * w + self.street_width + 1][self.offset * h + i] = TileFactory.create(TileFactory.WALL_TILE)
        for i in range(self.street_width):
            for j in range(self.street_width):
                self.tiles[self.offset * w + i + 1][self.offset * h + j + 1] = TileFactory.create(TileFactory.ROAD_TILE)

    def add_horizontal_road(self, node):
        (w, h) = node
        for i in range(self.street_length):
            self.tiles[self.offset * w + i + self.street_width + 1][self.offset * h] = TileFactory.create(TileFactory.WALL_TILE)
            self.tiles[self.offset * w + i + self.street_width + 1][self.offset * h + self.street_width + 1] = TileFactory.create(TileFactory.WALL_TILE)
            for j in range(self.street_width):
                self.tiles[self.offset * w + i + self.street_width + 1][self.offset * h + j + 1] = TileFactory.create(TileFactory.ROAD_TILE)

    def add_vertical_road(self, node):
        (w, h) = node
        for j in range(self.street_length):
            self.tiles[self.offset * w][self.offset * h + j + self.street_width + 1] = TileFactory.create(TileFactory.WALL_TILE)
            self.tiles[self.offset * w + self.street_width + 1][self.offset * h + j + self.street_width + 1] = TileFactory.create(TileFactory.WALL_TILE)
            for i in range(self.street_width):
                self.tiles[self.offset * w + i + 1][self.offset * h + j + self.street_width + 1] = TileFactory.create(TileFactory.ROAD_TILE)

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked
