import pygame
import settings
import player

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
        self.tip = tip
        self.hp = settings.BLOCK_HP[tip]
        self.__update_state()

    def damage(self):
        self.hp -= 2
        self.__update_state()
        if self.hp <= 0:
            self.kill()

    def __update_state(self):
        settings.BLOCK_IMAGE[self.tip]

        f = pygame.font.SysFont('arial', 25)
        f_render = f.render(str(self.hp), True, [0, 255, 0])
        self.image.blit(f_render, [0, 0])
