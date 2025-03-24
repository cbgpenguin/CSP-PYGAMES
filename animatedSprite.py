import pygame


class AnimatedSprite(pygame.sprite.Sprite):
        
        def __init__(self, screen, x, y, defaultFrames, frameRate):
            super().__init__()
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
            self.lastFrameUpdate = 0
            self.counter = 0
        
        #Changes and draws the image
        def update(self):
            delta = self.clock.tick() / 1000.0
            self.lastFrameUpdate = self.lastFrameUpdate + delta
            # print(self, "frame update:", self.lastUpdate)
            if self.lastFrameUpdate >= (1.0 / self.frame_rate):
                # For example have a frame rate of 6 fps: (1/6 = 0.16666) so if its been longer go to next frame
                self.newFrame()

            newPos = self.rect.move(self.movePos)
            if self.area.contains(newPos): 
                self.rect = newPos
                pygame.event.pump()
            
            # print("state:", self.state)

            #actually draws the image onto the position
            self.screen.blit(self.image, self.rect)

            

        def newFrame(self):
            self.lastFrameUpdate = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]

            if self.state == "moveLeft":
                self.image = pygame.transform.flip(self.image, True, False)
                print("flipping")
                self.isFlipped = True

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
