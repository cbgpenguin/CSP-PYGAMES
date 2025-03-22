import pygame


class AnimatedSprite(pygame.sprite.Sprite):
        
        def __init__(self, screen, x, y, defaultFrames, frameRate):
            super().__init__()
            self.isFlipped = False
            self.screen = screen
            self.image = defaultFrames[0]
            self.rect = self.image.get_rect(topleft=(x, y))
            self.defaultFrames = defaultFrames
            self.frames = defaultFrames
            self.frame_index = 0
            self.frame_rate = frameRate
            self.frame_counter = 0
            self.movePos = [0, 0]
            self.area = screen.get_rect()
            self.speed = 6
            self.state = "still"
            self.clock = pygame.time.Clock()
            self.lastUpdate = 0
        
        def update(self):
            print(self.isFlipped)
            delta = self.clock.tick() / 1000.0
            self.lastUpdate = self.lastUpdate + delta
            # print(self, "frame update:", self.lastUpdate)
            if self.lastUpdate >= (1.0 / self.frame_rate):
                # For example have a frame rate of 6 fps: (1/6 = 0.16666) so if its been longer go to next frame
                self.lastUpdate = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]

            newPos = self.rect.move(self.movePos)
            if self.area.contains(newPos):
                self.rect = newPos
                pygame.event.pump()
            print("state:", self.state)

            if self.state == "moveLeft" and self.isFlipped == False:
                self.image = pygame.transform.flip(self.image, True, False)
                print("flipping")
                self.isFlipped = True
            elif self.state != "moveLeft" and self.isFlipped == True:
                self.image = pygame.transform.flip(self.image, True, False)
                print("unFlipping!")
                self.isFlipped = False

        def changeAnimation(self, newFrames):
            self.frames = newFrames
        
        def defaultAnimation(self):
            self.frames = self.defaultFrames

        def moveLeft(self):
            self.movePos[0] = self.movePos[0] - (self.speed)
            self.state = "moveLeft"

        def moveRight(self):
            self.movePos[0] = self.movePos[0] + (self.speed)
            self.state = "moveRight"
                
        def draw(self):
            self.screen.blit(self.image, self.rect)
