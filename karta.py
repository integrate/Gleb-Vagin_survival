import pygame
import settings
import blocks
import json


def save_map():
    open_open = open("save_karta.json", 'w+')

    spisok_sprites = group_sprite.sprites()
    bab = []
    for s in spisok_sprites:
        block_slovar = {
            'x': s.rect.x,
            'y': s.rect.y,
            'tip': s.tip
        }
        bab.append(block_slovar)

    json.dump(bab, open_open, indent=4)
    open_open.close()


def set_block(block_x, block_y, tip):
    x = 37 * block_x
    y = 36 * block_y
    dgsgdysg = blocks.Block(x, y, tip)
    group_sprite.add(dgsgdysg)


def proshetka(x, y):
    block_x = x // 37
    block_y = y // 36
    return [block_x, block_y]


print(__file__)
# подготавливаем библиотеку
pygame.init()
print(pygame.display.get_driver())
pygame.mixer.init()  # для звука

clock = pygame.time.Clock()

# создаём окно
screen = pygame.display.set_mode((0, 0))
settings.SCREEN_WIDTH = screen.get_width()
settings.SCREEN_HEIGHT = screen.get_height()
pygame.display.set_caption("карта, просто карта")

# СОЗДАЁМ КНОПКУ
knopka_font = pygame.font.SysFont('arial', 35)
knopka_font_surf = knopka_font.render("сохранить", False, [155, 174, 0])
knopka_width = knopka_font_surf.get_width()
knopka_height = knopka_font_surf.get_height()

knopka = pygame.Rect(0, 0, knopka_width, knopka_height)

group_sprite = pygame.sprite.Group()
running = True
while running:
    # задержка
    clock.tick(60)

    new_events = pygame.event.get()
    for event in new_events:

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            a = knopka.collidepoint(event.pos[0], event.pos[1])
            if a == 0:
                yuiop = proshetka(event.pos[0], event.pos[1])
                set_block(yuiop[0], yuiop[1], blocks.BLOCK_TYPE_STONE)
            else:
                save_map()

        if event.type == pygame.QUIT:
            running = False
    # ОТРИСОВКА
    screen.fill([255, 0, 0])
    pygame.draw.rect(screen, [228, 228, 228], knopka, 0)
    screen.blit(knopka_font_surf, knopka)
    group_sprite.draw(screen)
    pygame.display.flip()
