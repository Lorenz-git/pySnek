import os

import pygame
from typing import Tuple, List

from core.constants import COLOR_SNAKE, TILE_SIZE, RESOURCES_DIR
from core.utils import grid_to_pixel_coord


class Snake:
    def __init__(self, grid_pos: Tuple[int, int]):
        self.segments: List[Tuple[int, int]] = [grid_pos, (4, 5), (3, 5), (3, 4)]
        self.direction = (1, 0)
        self.last_direction = self.direction
        self.new_segment = None
        self.head_texture = None
        self.head_texture_right = None
        self.head_texture_up = None
        self.head_texture_left = None
        self.head_texture_down = None


    def create_textures(self):
        self.head_texture_up = pygame.image.load(os.path.join(RESOURCES_DIR, 'head.png')).convert_alpha()
        self.head_texture_up = pygame.transform.scale(self.head_texture_up, (TILE_SIZE - 1, TILE_SIZE - 1))
        self.head_texture_left = pygame.transform.rotate(self.head_texture_up, 90)
        self.head_texture_down = pygame.transform.rotate(self.head_texture_left, 90)
        self.head_texture_right = pygame.transform.rotate(self.head_texture_down, 90)
        self.head_texture = self.head_texture_right


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i] = (self.segments[i - 1][0], self.segments[i - 1][1])
        self.segments[0] = (self.segments[0][0] + self.direction[0], self.segments[0][1] + self.direction[1])

        # append stored new segment if there is one
        if self.new_segment is not None:
            self.segments.append(self.new_segment)
        self.last_direction = self.direction
        self.new_segment = None

    def draw(self, screen):
        # draw head
        screen.blit(self.head_texture, pygame.Rect(*grid_to_pixel_coord(self.segments[0]), TILE_SIZE - 1, TILE_SIZE - 1))
        # draw rest
        for seg in self.segments[1:]:
            pygame.draw.rect(screen, COLOR_SNAKE, pygame.Rect(*grid_to_pixel_coord(seg), TILE_SIZE - 1, TILE_SIZE - 1))

    def up(self):
        if self.last_direction != (0, 1):
            self.direction = (0, -1)
            self.head_texture = self.head_texture_up

    def down(self):
        if self.last_direction != (0, -1):
            self.direction = (0, 1)
            self.head_texture = self.head_texture_down

    def left(self):
        if self.last_direction != (1, 0):
            self.direction = (-1, 0)
            self.head_texture = self.head_texture_left

    def right(self):
        if self.last_direction != (-1, 0):
            self.direction = (1, 0)
            self.head_texture = self.head_texture_right
