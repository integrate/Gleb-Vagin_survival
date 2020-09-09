import pygame
import settings
import player

BLOCK_TYPE_GROUND = 1
BLOCK_TYPE_WOOD = 2
BLOCK_TYPE_STONE = 3


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
        if self.hp <= settings.BLOCK_HP[self.tip] / 2:
            self.image = settings.BLOCK_IMAGE_BROKEN[self.tip].copy()
        else:
            self.image = settings.BLOCK_IMAGE[self.tip].copy()

        f = pygame.font.SysFont('arial', 25)
        f_render = f.render(str(self.hp), True, [0, 255, 0])
        self.image.blit(f_render, [0, 0])
