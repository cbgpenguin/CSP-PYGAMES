import pygame

class menu(pygame.sprite.Sprite):
        def __init__(self, screen, x, y, image, name):
            super().__init__()
            self.rect = (x, y)
            self.screen = screen
            self.image = image
            self.name = name
            self.isOpen = False

        def open(self):
              self.isOpen = True
              