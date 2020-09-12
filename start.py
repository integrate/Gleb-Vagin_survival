import pygame, player, blocks, settings, math

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
settings.SCREEN_WIDTH = screen.get_width()
settings.SCREEN_HEIGHT = screen.get_height()
pygame.display.set_caption("Survival")
clock = pygame.time.Clock()
t = blocks.Block(200, 920, blocks.BLOCK_TYPE_STONE)
g = blocks.Block(500, 805, blocks.BLOCK_TYPE_WOOD)
r = blocks.Block(400, 600, blocks.BLOCK_TYPE_GROUND)
group_blocks = pygame.sprite.Group()
group_blocks.add(t, g, r)
group_sprite = pygame.sprite.Group()
p = player.Player('name', settings.SCREEN_WIDTH / 2, 0)
group_sprite.add(p, t, g, r)
# Фон игры
image = pygame.image.load('assets/1_37.png')
image_rect = image.get_rect()
fon = pygame.Surface([settings.SCREEN_WIDTH + image_rect.width, settings.SCREEN_HEIGHT])
k = 0
while k <= settings.SCREEN_WIDTH + image_rect.width:
    fon.blit(image, [k, 0])
    k += image_rect.width

scr = 0
# Цикл игры
running = True
while running:
    clock.tick(60)

    scr += 0
    u = round(scr) % image_rect.width
    # fon.scroll(-1, 0)

    # Ввод процесса (события)
    new_events = pygame.event.get()
    for event in new_events:

        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
            # Проверка попали мы по блоку или нет
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            blocks = group_blocks.sprites()
            for block in blocks:
                if block.rect.collidepoint(event.pos):
                    rastoyanie = math.dist(p.rect.center, block.rect.center)
                    if rastoyanie < 250:
                        block.damage()
    keyboard = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    if keyboard[pygame.K_SPACE] == 1:
        p.jump()
    elif keyboard[pygame.K_d] == 1:
        p.speed_x = 5
        scr += 10
    elif keyboard[pygame.K_a] == 1:
        p.speed_x = - 5
        scr -= 10
    else:
        p.speed_x = 0

    # Обновление
    p.update(group_blocks)
    # Рендеринг
    screen.fill([0, 0, 0])
    screen.blit(fon, [-u, 0])
    group_sprite.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
