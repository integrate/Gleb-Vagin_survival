import pygame
import settings

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

running = True
while running:
    # задержка
    clock.tick(60)
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("привет")
        if event.type == pygame.QUIT:
            running = False
