# Consts for the game

from typing import Tuple


class Consts:
    # Color
    BACKGROUND : str = "yellow"
    BIRD_COLOR : str = "red"
    WALL_COLOR : str = "black"
    # Size
    WIDTH : int = 400
    HIGHT : int = 600
    # Bird diameter
    BIRD_DIAMETER : int = 15
    BIRD_RADIOS : float = BIRD_DIAMETER / 2
    # Bird start location
    BIRD_START_XY : Tuple = (0, HIGHT/2)
    BIRD_START : Tuple = (
            BIRD_START_XY[0],
            BIRD_START_XY[1] - BIRD_RADIOS,
            BIRD_START_XY[0] + BIRD_DIAMETER,
            BIRD_START_XY[1] + BIRD_RADIOS
            )
    # Frame rate
    FRAME_RATE : float = 0.01
    # Time delay for closing the window
    CLOSE_WINDOW : float = 1000
    # Bird movement
    VX : int = 2
    VY : float = 1
    A : float = 0.5

