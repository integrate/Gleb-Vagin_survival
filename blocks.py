import pygame, settings

BLOCK_TYPE_GROUND = 1
BLOCK_TYPE_WOOD = 2
BLOCK_TYPE_STONE = 3

BLOCK_IMAGE_GROUND = pygame.image.load("assets/blocks/ground.jpg")
BLOCK_IMAGE_STONE = pygame.image.load("assets/blocks/stone.png")
BLOCK_IMAGE_WOOD = pygame.image.load("assets/blocks/wood.png")


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, tip):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 37, 36)
        self.image = pygame.image.load('assets/blocks/ground.jpg')

        if tip == BLOCK_TYPE_GROUND:
            self.hp = settings.HP_GROUND
        elif tip == BLOCK_TYPE_WOOD:
            self.hp = settings.HP_WOOD
        elif tip == BLOCK_TYPE_STONE:
            self.hp = settings.HP_STONE
