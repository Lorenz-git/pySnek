import os

GRID_SIZE = 800
WINDOW_SIZE = GRID_SIZE + 1
CELLS = 10
TILE_SIZE = GRID_SIZE // CELLS
FPS = 5
COLOR_LINE = [255, 255, 255]
COLOR_BG = [0, 0, 0]
COLOR_SNAKE = [3, 68, 254]
COLOR_ITEM = [0, 255, 0]

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "..", "resources")
