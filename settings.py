import blocks
import pygame
import utilite

GROUND_HEIGHT = 841
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

BLOCK_HP = {
    blocks.BLOCK_TYPE_GROUND: 15,
    blocks.BLOCK_TYPE_STONE: 100,
    blocks.BLOCK_TYPE_WOOD: 35}
BLOCK_IMAGE = {
    blocks.BLOCK_TYPE_GROUND: pygame.image.load(utilite.get_path("assets/blocks/ground.jpg")),
    blocks.BLOCK_TYPE_WOOD: pygame.image.load(utilite.get_path("assets/blocks/wood.png")),
    blocks.BLOCK_TYPE_STONE: pygame.image.load(utilite.get_path("assets/blocks/stone.png"))}

BLOCK_IMAGE_BROKEN = {
    blocks.BLOCK_TYPE_GROUND: pygame.image.load(utilite.get_path("assets/blocks/broken_ground.jpg")),
    blocks.BLOCK_TYPE_WOOD: pygame.image.load(utilite.get_path("assets/blocks/broken_wood.png")),
    blocks.BLOCK_TYPE_STONE: pygame.image.load(utilite.get_path("assets/blocks/broken_stone.png"))}

# Растояние удара
HIT_DISTANCE = 250
