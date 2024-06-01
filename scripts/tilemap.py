import json
from typing import Dict

from scripts.elements import Element

FILE_PATH = "data/maps/tilemap.json"
class Tilemap:
    def __init__(self, game, tile_size=50):
        self.game = game
        self.tile_size = tile_size
        self.tilemap : Dict[str,Element] = {}

    def save(self):
        f = open(FILE_PATH, 'w')
        elements  = []
        for tile in self.tilemap.values():
            elements.append(
                {
                    "position":[tile.pos[0]*50, tile.pos[1]*50],
                    "type":tile.type,
                    "subtype":tile.subtype
                }
            )

        json.dump(elements, f)
        f.close()
        
    def load(self):
        f = open(FILE_PATH, 'r')
        map_data = json.load(f)
        f.close()

        for tile in map_data:
            x = tile["position"][0]//50
            y = tile["position"][1]//50
            self.tilemap[str(x)+';'+str(y)] = Element([x,y], tile["type"], tile["subtype"])

        print(self.tilemap)
    def render(self, surf, offset=(0, 0)):

        for x in range(offset[0] // self.tile_size, (offset[0] + surf.get_width()) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (offset[1] + surf.get_height()) // self.tile_size + 1):
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.game.assets[tile.type][tile.subtype]["image"], (tile.pos[0] * self.tile_size - offset[0], tile.pos[1] * self.tile_size - offset[1]))