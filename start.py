import pygame, player, blocks, settings

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Survival")
clock = pygame.time.Clock()
t = blocks.Block(200, 914)
g = blocks.Block(500, 805)
group_blocks = pygame.sprite.Group()
group_blocks.add(t, g)
group_sprite = pygame.sprite.Group()
p = player.Player('name', settings.SCREEN_WIDTH/2, 0)
group_sprite.add(p, t, g)
# Фон игры
image = pygame.image.load('C:/Users/#MOB/PycharmProjects/Projects/assets/1_37.png')
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

    scr += 1
    u = round(scr) % image_rect.width
    # fon.scroll(-1, 0)

    # Ввод процесса (события)
    new_events = pygame.event.get()
    for event in new_events:

        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    a = pygame.key.get_pressed()

    if a[pygame.K_SPACE] == 1:
        p.jump()
    elif a[pygame.K_d] == 1:
        p.speed_x = 5
        # scr += 5
    elif a[pygame.K_a] == 1:
        p.speed_x = - 5
        # scr -= 5
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
