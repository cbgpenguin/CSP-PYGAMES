    

import pygame


class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, screen, x, y, defaltFrames, frameRate):
            super().__init__()
            self.screen = screen
            self.image = defaltFrames[0]
            self.rect = self.image.get_rect(topleft=(x, y))
            self.defaltFrames = defaltFrames
            self.frames = defaltFrames
            self.frame_index = 0
            self.frame_rate = frameRate
            self.frame_counter = 0
            self.movepos = [0,0]
            self.area = screen.get_rect()
            self.speed = 6
            self.state = "still"
            self.clock = pygame.time.Clock()
            self.lastUpdate = 0


        
        def update(self):
            delta = self.clock.tick() / 1000.0
            self.lastUpdate = self.lastUpdate + delta
            print(self, "frame update:", self.lastUpdate)
            if self.lastUpdate >= (1.0/self.frame_rate):
                # For example have a frame rate of 6 fps: (1/6 = 0.16666) so if its been longer go to next frame
                self.lastUpdate = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]
            newpos = self.rect.move(self.movepos)
            if self.area.contains(newpos):
                self.rect = newpos
                pygame.event.pump()

        def changeAnimation(self, newFrames):
             self.frames = newFrames
        
        def defaltAnimation(self):
             self.frames = self.defaltFrames

        def moveLeft(self):
            self.movepos[0] = self.movepos[0] - (self.speed)
            self.state = "moveLeft"

        def moveRight(self):
            self.movepos[0] = self.movepos[0] + (self.speed)
            self.state = "moveRight"
                
        def draw(self):
            self.screen.blit(self.image, self.rect)