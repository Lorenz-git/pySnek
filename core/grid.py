import array
from itertools import product
from random import seed, randint
from typing import Tuple

import pygame

from core.constants import TILE_SIZE, COLOR_LINE, COLOR_BG, WINDOW_SIZE, CELLS, COLOR_ITEM
from core.snake import Snake
from core.utils import grid_to_pixel_coord


class Grid:
    def __init__(self):
        self.items = []
        self.background = None
        self.snake = None
        seed(1)

    def add_snake(self, snake: Snake):
        self.snake = snake

    def create_background(self):
        board_data = []
        for x, y in product(range(WINDOW_SIZE), repeat=2):
            if x % TILE_SIZE == 0 or y % TILE_SIZE == 0:
                board_data.extend(COLOR_LINE)
            else:
                board_data.extend(COLOR_BG)
        board_data = array.array("B", board_data)
        self.background = pygame.image.frombuffer(board_data, (WINDOW_SIZE, WINDOW_SIZE), "RGB")

    # random chance of item being spawned
    def generate_items(self):
        if randint(0, 6) == 5:
            self.items.append(self.get_random_empty_cell())

    def get_random_empty_cell(self) -> Tuple[int, int]:
        cell = (randint(0, CELLS - 1), randint(0, CELLS - 1))
        while not self.is_cell_empty(cell):
            cell = (randint(0, CELLS - 1), randint(0, CELLS - 1))
        return cell

    def is_cell_empty(self, cell: Tuple[int, int]):
        for seg in self.snake.segments:
            if seg == cell:
                return False
        for item in self.items:
            if seg == item:
                return False
        return True

    def draw(self, screen):
        # draw background
        screen.blit(self.background, self.background.get_rect())

        # draw items
        for item in self.items:
            pygame.draw.rect(screen, COLOR_ITEM, pygame.Rect(*grid_to_pixel_coord(item), TILE_SIZE - 1, TILE_SIZE - 1))

    def feed_snake(self):
        for item in self.items:
            if item == self.snake.segments[0]:
                self.items.remove(item)
                self.snake.new_segment = self.snake.segments[len(self.snake.segments) - 1]

    def rip_snake(self):
        if not (0 <= self.snake.segments[0][0] < CELLS and 0 <= self.snake.segments[0][1] < CELLS):
            return True
        for seg in self.snake.segments[1:]:
            if self.snake.segments[0] == seg:
                return True
        return False

