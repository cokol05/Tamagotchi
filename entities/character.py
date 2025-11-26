"""
В этом модуле персонаж собирается из картинок.
"""

from pygame import image
import os


class Character:
    """
    Класс для создания персонажа.
    """
    def __init__(self, image_path):
        self.image = image.load(image_path)
        pass






































import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# background = pygame.image.load("resources/main.background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0, 0, 0))
    # screen.blit(background, (0, 0))
    # pygame.draw.circle(screen, (121, 143, 209), (400, 300), 100)

    # pygame.draw.polygon(screen, (121, 143, 209), ((380, 200), (400, 170), (420, 200)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
