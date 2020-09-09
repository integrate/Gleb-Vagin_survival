import blocks
import pygame

GROUND_HEIGHT = 841
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

BLOCK_HP = {
    blocks.BLOCK_TYPE_GROUND: 15,
    blocks.BLOCK_TYPE_STONE: 100,
    blocks.BLOCK_TYPE_WOOD: 35}
BLOCK_IMAGE = {
    blocks.BLOCK_TYPE_GROUND: pygame.image.load("assets/blocks/ground.jpg"),
    blocks.BLOCK_TYPE_WOOD: pygame.image.load("assets/blocks/wood.png"),
    blocks.BLOCK_TYPE_STONE: pygame.image.load("assets/blocks/stone.png")}

BLOCK_IMAGE_BROKEN = {
    blocks.BLOCK_TYPE_GROUND: pygame.image.load("assets/blocks/broken_ground.jpg"),
    blocks.BLOCK_TYPE_WOOD: pygame.image.load("assets/blocks/broken_wood.png"),
    blocks.BLOCK_TYPE_STONE: pygame.image.load("assets/blocks/broken_stone.png")}
