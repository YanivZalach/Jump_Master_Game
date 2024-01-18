# Generating a new walls location
import random
import time
# The gui engine
from tkinter import Canvas, Tk
from typing import List

from .window import Window

# The game consts
from .const import Consts, wallesCreate

# Function that move the game
class Move:
    # Function to move the bird
    @staticmethod
    def moveBird(canvas,bird):
        b_coords = canvas.coords(bird) # Coordinates of the bird
        # Updating VY
        Consts.VY += Consts.A  # V = V0 + AT
        # Did we got to the end of this side?
        # Width
        if b_coords[0] < 0 or b_coords[2] >= Consts.WIDTH:
            Consts.VX *= -1  # Change direction
        canvas.move(bird, Consts.VX, Consts.VY)

    @staticmethod
    # Making to bird going up
    def jump():
        Consts.VY = Consts.JUMP

    @staticmethod
    # Checking the bird is in the limits of the game
    def birdLimits(canvas,bird) -> bool:
        b_coords = canvas.coords(bird) # Coordinates of the bird
        if b_coords[1] < 0 or b_coords[3] >= Consts.HIGHT:
            return True
        return False  # Didn't passed the limits

    @staticmethod
    def moveWalls(canvas,walls:List,side):
        # Getting the relevant information on the 2 sides(y2)
        walls_cords = [canvas.coords(wall)[3] for index, wall in enumerate(walls) if index % 2 == 0]

        # Random new coords
        new_coords = (Consts.HIGHT - Consts.WALL_SPACE) * random.random()

        # Deleting the current walls
        canvas.delete(*walls)

        if side == "l": # The left side
            return Window.drowWalls(canvas, wallesCreate(walls_cords[0],new_coords))
            
        # For the right side
        return Window.drowWalls(canvas, wallesCreate(new_coords,walls_cords[1]))

    @staticmethod
    def toMoveWalles(canvas, walls:List, start_time) -> List:
        # Currant time
        c_time = time.time() - start_time
        # Change the left wall
        if c_time > Consts.WALLS_SWITCH_STERT_L:
            Consts.WALLS_SWITCH_STERT_L += Consts.WALL_CYCLE
            print("Switching left wall")
            return Move.moveWalls(canvas, walls, "l")
        # Changing the right wall
        if c_time > Consts.WALLS_SWITCH_START_R:
            Consts.WALLS_SWITCH_START_R += Consts.WALL_CYCLE
            print("Switching right wall")
            return Move.moveWalls(canvas, walls, "r")

        return walls


    @staticmethod
    # Checking the bird is in the limits of the game
    def wallLimits(canvas,bird,walls) -> bool:
        b_coords = canvas.coords(bird) # Coordinates of the bird
        walls_cords = [canvas.coords(wall)[3] for index, wall in enumerate(walls) if index % 2 == 0]  # Getting the relevant information on the 2 sides(y2)
        # On the left wall
        if b_coords[0] < Consts.WALL_X_COORDS[0]:
            if not (b_coords[1] > walls_cords[0] and b_coords[1] + Consts.BIRD_DIAMETER < walls_cords[0] + Consts.WALL_SPACE):
                return True

        # On the right wall
        if b_coords[2] > Consts.WALL_X_COORDS[1]:
            if not (b_coords[1] > walls_cords[1] and b_coords[1] + Consts.BIRD_DIAMETER < walls_cords[1] + Consts.WALL_SPACE):
                return True

        return False  # Didn't passed the limits

    @staticmethod
    # Checking the bird is in the limits of the game
    def limits(canvas,bird,walls) -> bool:  # One True and we lost the game
        return Move.wallLimits(canvas,bird,walls) or Move.birdLimits(canvas,bird)
