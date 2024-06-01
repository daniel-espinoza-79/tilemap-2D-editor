import sys

import pygame
from pygame import transform
from scripts.elements import Element
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('EDITION SPIKE')
        self.screen = pygame.display.set_mode((1600, 900))
        self.display = pygame.Surface((1600, 900))

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False,False,False]
        from scripts.config import assets        
        self.assets = assets
        self.tile_list = list(self.assets)
        self.subtypes_list  = {}
        for i in self.tile_list:
            self.subtypes_list[i] = list(self.assets[i])

        self.tyle_type = 0
        self.tyle_subtype = 0
        
        self.tilemap = Tilemap(self, tile_size=50)
        try:
            self.tilemap.load()
        except FileNotFoundError:
            pass
        
        self.scroll = [0, 0]

        self.clicking = False
        self.right_clicking = False
        self.shift = False     
        self.delete = False
    def run(self):
        while True:
            self.display.fill((0,0,0))
            
            self.scroll[0]+= (self.movement[1] - self.movement[0]) * 10
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            self.tilemap.render(self.display, offset=render_scroll)

            type = self.tile_list[self.tyle_type]
            subtype = self.subtypes_list[type][self.tyle_subtype]
            curr_tyle_img = self.assets[type][subtype]["image"].copy()
            curr_tyle_img.set_alpha(100)


            mouse_pos = pygame.mouse.get_pos()
            tile_pos = ((mouse_pos[0]+self.scroll[0])// 50, (mouse_pos[1]+self.scroll[1]) // 50)


            self.display.blit(curr_tyle_img, (tile_pos[0]*50-self.scroll[0], tile_pos[1]*50-self.scroll[1]))

            if self.clicking:
                contains = self.tilemap.tilemap.get(str(tile_pos[0])+';'+str(tile_pos[1]))
                if self.delete:
                    if contains:
                        del self.tilemap.tilemap[str(tile_pos[0])+';'+str(tile_pos[1])]
                else :
                    if not contains:
                        self.tilemap.tilemap[str(tile_pos[0])+';'+str(tile_pos[1])] = Element([tile_pos[0], tile_pos[1]], self.tile_list[self.tyle_type], self.subtypes_list[self.tile_list[self.tyle_type]][self.tyle_subtype],self.tyle_subtype)


            if self.right_clicking:
                if str(tile_pos[0])+';'+str(tile_pos[1]) in self.tilemap.tilemap:
                    del self.tilemap.tilemap[str(tile_pos[0])+';'+str(tile_pos[1])]


            self.display.blit(transform.scale(curr_tyle_img,(50,50)), (5,5))

            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            self.tilemap.render(self.display, offset=render_scroll)
   
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                    if event.button == 3:
                        self.right_clicking = True
                    if self.shift:
                        if event.button == 4:
                            self.tyle_subtype = (self.tyle_subtype-1)%len(self.assets[self.tile_list[self.tyle_type]])
                        if event.button == 5:
                            self.tyle_subtype = (self.tyle_subtype+1)%len(self.assets[self.tile_list[self.tyle_type]])
                    else:
                        if event.button == 4:
                            self.tyle_type = (self.tyle_type-1)%len(self.tile_list)
                            self.tyle_subtype = 0
                        if event.button == 5:
                            self.tyle_type = (self.tyle_type+1)%len(self.tile_list)
                            self.tyle_subtype = 0

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False
                    if event.button == 3:
                        self.right_clicking = False



                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                    if event.key == pygame.K_q:
                        self.delete = not self.delete
                    if event.key == pygame.K_s:
                        self.tilemap.save()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False
            
            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()