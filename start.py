import pygame, player, blocks, settings, math, utilite, os, json


def karta_load(gr, gs):
    print('типо загружаем карту')
    qwerty = open("save_karta.json", 'r')
    uiopas = json.load(qwerty)
    print(uiopas)
    for sapoiu in uiopas:
        print(sapoiu)
        sdx = blocks.Block(sapoiu['x'], sapoiu['y'], sapoiu['tip'])
        gs.add(sdx)
        gr.add(sdx)

    qwerty.close()


# os.environ['SDL_VIDEODRIVER'] = "directx"

print(__file__)
# подготавливаем библиотеку
pygame.init()
# print(pygame.display.get_driver())
pygame.mixer.init()  # для звука

# создаём окно
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0))
settings.SCREEN_WIDTH = screen.get_width()
settings.SCREEN_HEIGHT = screen.get_height()
settings.GROUND_HEIGHT = settings.SCREEN_HEIGHT-100
pygame.display.set_caption("Survival")

# часы
clock = pygame.time.Clock()

# создаём группу спрайтов
group_sprite = pygame.sprite.Group()
group_blocks = pygame.sprite.Group()
karta_load(group_blocks, group_sprite)
# создаём игрока
p = player.Player('name', settings.SCREEN_WIDTH / 2, 0)
group_sprite.add(p)

# Фон игры
image = pygame.image.load(utilite.get_path('assets/1_37.png'))
image_rect = image.get_rect()
fon = pygame.Surface([settings.SCREEN_WIDTH + image_rect.width, settings.SCREEN_HEIGHT])
k = 0
while k <= settings.SCREEN_WIDTH + image_rect.width:
    fon.blit(image, [k, 0])
    k += image_rect.width

# устанавливаем смещение фона
scr = 0
sdvig_x = 0

# Цикл игры
running = True
while running:
    # задержка
    clock.tick(60)

    # обрабатываем события
    new_events = pygame.event.get()
    for event in new_events:

        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # Проверка попали мы по блоку или нет
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = [event.pos[0] - sdvig_x, event.pos[1]]
            blocks = group_blocks.sprites()

            for block in blocks:
                if block.rect.collidepoint(pos):
                    rastoyanie = math.dist(p.rect.center, block.rect.center)
                    if rastoyanie < 250:
                        block.damage()
            # print(event.pos)

    # обработка событий клавиатуры
    keyboard = pygame.key.get_pressed()

    if keyboard[pygame.K_SPACE] == 1:
        p.jump()
    elif keyboard[pygame.K_d] == 1:
        p.speed_x = 5
        # scr += 10
    elif keyboard[pygame.K_a] == 1:
        p.speed_x = - 5
        # scr -= 10
    else:
        p.speed_x = 0

    # Обновление
    p.update(group_blocks)

    # Рендеринг
    u = round(scr) % image_rect.width
    screen.blit(fon, [-u, 0])
    # group_sprite.draw(screen)
    sprites = group_sprite.sprites()
    sdvig_x = settings.SCREEN_WIDTH / 2 - p.rect.centerx
    sdvig_x = int(sdvig_x)
    scr = - sdvig_x
    for sprite in sprites:
        r = sprite.rect.move(sdvig_x, 0)
        screen.blit(sprite.image, r)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
