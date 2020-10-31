from typing import Tuple

from core.constants import TILE_SIZE


def grid_to_pixel_coord(pos: Tuple[int, int]) -> Tuple[int, int]:
    return pos[0] * TILE_SIZE + 1, pos[1] * TILE_SIZE + 1
