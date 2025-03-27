import pygame

class pointOfInterest(pygame.sprite.Sprite):
        def __init__(self, screen, x, y, image, name):
            super().__init__()
            self.rect = (x, y)
            self.screen = screen
            self.image = image
            self.isPlayerInRange = False
            self.visibleRange = 50 #pixels
            self.name = name

        def update(self):
              pass
        
        def open(self):
              print("opening")
              self.screen