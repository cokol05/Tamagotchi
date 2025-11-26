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
