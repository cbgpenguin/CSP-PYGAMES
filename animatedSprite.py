import pygame


class AnimatedSprite(pygame.sprite.Sprite):
        
        def __init__(self, screen, x, y, defaultFrames, frameRate):
            super().__init__()
            self.screen = screen
            self.image = defaultFrames[0]
            self.rect = self.image.get_rect(topleft=(x, y))
            self.defaultFrames = defaultFrames
            self.frames = defaultFrames
            self.frameIndex = 0
            self.frame_rate = frameRate
            self.frame_counter = 0
            self.movePos = [0, 0]
            self.area = screen.get_rect()
            self.speed = 20 # in pixels per second
            self.state = "still"
            self.clock = pygame.time.Clock()
            self.lastFrameUpdate = 0
            self.delta = 0
        
        #Changes and draws the image
        def update(self):
            self.delta = (self.clock.tick() / 1000.0)
            print("updating... here's delta:", self.delta)
            self.lastFrameUpdate = self.lastFrameUpdate + self.delta
            # print(self, "frame update:", self.lastUpdate)
            if self.lastFrameUpdate >= (1.0 / self.frame_rate):
                # For example have a frame rate of 6 fps: (1/6 = 0.16666) so if its been longer go to next frame
                self.newFrame()

            if self.state == "moveLeft":
                self.moveLeft()
            if self.state == "moveRight":
                self.moveRight()

            newPos = self.rect.move(self.movePos)
            if self.area.contains(newPos): 
                self.rect = newPos
                pygame.event.pump()
            
            # print("state:", self.state)

            #actually draws the image onto the position
            self.screen.blit(self.image, self.rect)

            

        def newFrame(self):
            self.lastFrameUpdate = 0
            self.frameIndex = (self.frameIndex + 1) % len(self.frames)
            self.image = self.frames[self.frameIndex]

            if self.state == "moveLeft":
                self.image = pygame.transform.flip(self.image, True, False)
                # print("flipping")

        def changeAnimation(self, newFrames):
            self.frames = newFrames
        
        def defaultAnimation(self):
            self.frames = self.defaultFrames

        def moveLeft(self):
            # print("move left called")
            self.movePos[0] = self.movePos[0] - (self.speed * self.delta)
            # print("going left. Delta:", self.delta)
            # print("pixels to the left:", self.speed * self.delta)

        def moveRight(self):
            # print("move right called")
            self.movePos[0] = self.movePos[0] + (self.speed * self.delta)
            # print("going right. Delta:", self.delta)
            # print("pixels to the right:", self.delta * self.speed)