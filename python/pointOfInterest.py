import pygame
from menu import menu

class PointOfInterest(pygame.sprite.Sprite):
      def __init__(self, screen, x, y, image, name, text):
            super().__init__()
            self.rect = image.get_rect(topleft=(x, y))
            self.screen = screen
            self.image = image
            self.isPlayerInRange = False
            self.visibleRange = 70 #pixels
            self.name = name
            self.text = text
            self.isOpen = False
            self.menu = None
            
      def update(self):
            if self.isPlayerInRange:
                  self.screen.blit(self.image, pygame.Rect(self.rect.left + 60, self.rect.top, self.rect.right, self.rect.bottom))
            if self.isOpen:
                  self.menu.update()

      
      def open(self):
            print("opening")
            self.isOpen = True
            self.menu = menu(self.screen, self.name, self.text)

      def close(self):
            if self.isOpen == False:
                  return
            else:
                  self.isOpen = False
                  del self.menu

      