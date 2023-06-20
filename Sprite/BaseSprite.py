import pygame


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image, blood, weapon):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.blood = blood
        self.weapon = weapon

    def move_right(self):
        ...

    def move_left(self):
        ...

    def jump_up(self):
        ...

    def jump_below(self):
        ...
