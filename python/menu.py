import pygame

class menu(pygame.sprite.Sprite):
        def __init__(self, screen, name, text):
            super().__init__()
            self.rect = pygame.Rect(1075, 17, 400, 670)
            self.textColor = (150, 200, 200)
            self.screen = screen
            self.name = name
            self.lines = text
            print("menu", self.name, "open")

        def update(self):
            print("updating menu", self.name)
            self.screen.fill((210, 160, 50), pygame.Rect(self.rect.left - 5, self.rect.top - 5, 415, 680))
            self.screen.fill((40, 40, 50), self.rect)

            font = pygame.font.Font(None, 40)
            for i in range(len(self.lines)):
                wordPos = pygame.Rect(self.rect.left + 10, self.rect.top + 20 + (30 * i), self.rect.right - 20, self.rect.bottom - 30) 
                self.screen.blit(font.render(self.lines[i], 1, self.textColor), wordPos)
            self.screen.blit(font.render("Keep walking to find evidence", 1, self.textColor), pygame.Rect(self.rect.left, self.rect.top + 640, self.rect.right, self.rect.bottom))
            # self.screen.blit(self.image, self.rect)
