# Consts for the game

from typing import Tuple


class Consts:
    # Debug mode
    DEBUG : bool = False
    # Color
    BACKGROUND : str = "yellow"
    BIRD_COLOR : str = "red"
    WALL_COLOR : str = "black"
    # Size
    WIDTH : int = 400
    HIGHT : int = 600
    HIGHT_WITH_LABAL : int = 700
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
    # Walls specifications
    WALL_WIDTH : int = 20
    WALL_SPACE : int = BIRD_DIAMETER * 9
    WALLS_START_Y : float = (HIGHT / 2) - (WALL_SPACE / 2)
    # For the hitting
    WALL_X_COORDS : Tuple = (WALL_WIDTH, WIDTH - WALL_WIDTH)  # The x limits to check
    # Frame rate
    FRAME_RATE : float = 0.01
    # Time delay for closing the window
    CLOSE_WINDOW : float = 1000
    # Bird movement
    VX_O : int = 2
    VX : int = VX_O
    VY_O : float = 0.5 * HIGHT / (WIDTH/VX)  # So it will have the time to get from top to bottom in a round (Physics) * 0.5
    VY : float = VY_O
    A : float = 2 * 2 * HIGHT / (WIDTH/VX)**2
    JUMP : float = -70*A 
    # Time to switch walls
    WALLS_SWITCH : float = (FRAME_RATE/2 + (WIDTH / VX)/2) / 100  # For the python time module, the FRAME_RATE is for synchronising
    # The starting times
    WALLS_SWITCH_STERT_L_O : float = WALLS_SWITCH * 4
    WALLS_SWITCH_START_R_O : float = WALLS_SWITCH * 2
    WALLS_SWITCH_STERT_L : float = WALLS_SWITCH * 4
    WALLS_SWITCH_START_R : float = WALLS_SWITCH * 2
    # The change cycle
    WALL_CYCLE : float = WALLS_SWITCH * 4
    # Label style
    FONT : Tuple= ('david', 20)
    LABEL_COLOR : str = 'white'
    LABEL_TEXT_COLOR : str = 'black'
    WIDTH_LABEL : int = round(WIDTH /15)
    HIGHT_LABEL : int = round(HIGHT_WITH_LABAL /250)

# Walls location
def wallesCreate(left=Consts.WALLS_START_Y, right=Consts.WALLS_START_Y):
    return (
        (  # Wall 1
            0,
            0,
            Consts.WALL_WIDTH,
            left
        ),
        (  # Wall 2
            0,
            left + Consts.WALL_SPACE,
            Consts.WALL_WIDTH,
            Consts.HIGHT
        ),
        (  # Wall 3
            Consts.WIDTH - Consts.WALL_WIDTH,
            0,
            Consts.WIDTH,
            right
        ),
        (  # Wall 4
            Consts.WIDTH - Consts.WALL_WIDTH,
            right + Consts.WALL_SPACE,
            Consts.WIDTH,
            Consts.HIGHT
        ),
    )

# Stating location
WALLS_START : Tuple = wallesCreate()
