import pygame, settings

BLOCK_TYPE_GROUND = 1
BLOCK_TYPE_WOOD = 2
BLOCK_TYPE_STONE = 3

BLOCK_IMAGE


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, tip):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 37, 36)
        self.image = pygame.image.load('C:/Users/#MOB/PycharmProjects/Projects/assets/ground.jpg')

        if tip == BLOCK_TYPE_GROUND:
            self.hp = settings.HP_GROUND
        elif tip == BLOCK_TYPE_WOOD:
            self.hp = settings.HP_WOOD
        elif tip == BLOCK_TYPE_STONE:
            self.hp = settings.HP_STONE
