import pygame

class pointOfInterest(pygame.sprite.Sprite):
        def __init__(self, screen, x, y, image, name):
            super().__init__()
            self.rect = (x, y)
            self.screen = screen
            self.image = image
            self.isPlayerInRange = False
            self.visibleRange = 30 #pixels
            self.name = name

        def update(self):
              from main import playerSprite
              if abs(playerSprite.rect[0] - self.rect[0]) < self.visibleRange:
                    print("player is close to", self.name)
                    self.isPlayerInRange = True