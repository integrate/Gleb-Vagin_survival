import pygame
import settings
import blocks

print(__file__)
# подготавливаем библиотеку
pygame.init()
print(pygame.display.get_driver())
pygame.mixer.init()  # для звука

clock = pygame.time.Clock()

# создаём окно
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1000, 750))
settings.SCREEN_WIDTH = screen.get_width()
settings.SCREEN_HEIGHT = screen.get_height()
pygame.display.set_caption("карта, просто карта")

# СОЗДАЁМ КНОПКУ
knopka_font = pygame.font.SysFont('arial', 35)
knopka_font_surf = knopka_font.render("сохранить", False, [155, 174, 0])
knopka_width = knopka_font_surf.get_width()
knopka_height = knopka_font_surf.get_height()

knopka = pygame.Rect(0, 0, knopka_width, knopka_height)
pygame.draw.rect(screen, [228, 228, 228], knopka, 0)
screen.blit(knopka_font_surf, knopka)


running = True
while running:
    # задержка
    clock.tick(60)

    new_events = pygame.event.get()
    for event in new_events:

        group_sprite = pygame.sprite.Group()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            block = blocks.Block(event.pos[0], event.pos[1], blocks.BLOCK_TYPE_GROUND)
            group_sprite.add(block)
            group_sprite.draw(screen)

        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
