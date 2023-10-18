import pygame
import sys

# Initialize pygame
pygame.init()
# Fonts
font = pygame.font.Font(None, 36)

# GUI Button class
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.clicked = True
        return self.clicked