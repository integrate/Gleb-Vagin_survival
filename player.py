import pygame, settings

PLAYER_STATE_STAND = 1
PLAYER_STATE_DOWN = 2
PLAYER_STATE_UP = 3

PLAYER_IMAGE_STAND = pygame.image.load('assets/player_stand.png')
PLAYER_IMAGE_DOWN = pygame.image.load('assets/player_down.png')
PLAYER_IMAGE_UP = pygame.image.load('assets/player_up.png')


class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 85, 92)
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_y = 0
        self.speed_x = 0
        self.state = PLAYER_STATE_STAND
        self.__update_state()

    def __update_state(self):
        if self.state == PLAYER_STATE_STAND:
            self.image = PLAYER_IMAGE_STAND
        elif self.state == PLAYER_STATE_UP:
            self.image = PLAYER_IMAGE_UP
        elif self.state == PLAYER_STATE_DOWN:
            self.image = PLAYER_IMAGE_DOWN

    def jump(self):
        if self.state == PLAYER_STATE_STAND:
            self.speed_y = - 60

    def update(self, group_blocks):
        self.speed_y += 4
        if self.speed_y < 0:
            self.state = PLAYER_STATE_UP
        if self.speed_y > 0:
            self.state = PLAYER_STATE_DOWN
        # if self.speed_x < 3:
        #     self.speed_x += 1

        self.rect.y += self.speed_y
        f = pygame.sprite.spritecollideany(self, group_blocks)
        if f is not None:
            if self.speed_y > 0:
                self.rect.bottom = f.rect.top
                self.state = PLAYER_STATE_STAND

            if self.speed_y < 0:
                self.rect.top = f.rect.bottom
            self.speed_y = 0

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > settings.GROUND_HEIGHT:
            self.rect.bottom = settings.GROUND_HEIGHT
            self.speed_y = 0
        if self.rect.bottom == settings.GROUND_HEIGHT:
            self.state = PLAYER_STATE_STAND

        self.rect.x += self.speed_x
        f = pygame.sprite.spritecollideany(self, group_blocks)
        if f is not None:
            if self.speed_x > 0:
                self.rect.right = f.rect.left
            if self.speed_x < 0:
                self.rect.left = f.rect.right

        if self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.__update_state()