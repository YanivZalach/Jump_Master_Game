# The gui engine
from tkinter import Canvas, Tk

# The game consts
from .const import Consts

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
    def Jump():
        Consts.VY = Consts.JUMP

    @staticmethod
    # Checking the bird is in the limits of the game
    def Limits(canvas,bird) -> bool:
        b_coords = canvas.coords(bird) # Coordinates of the bird
        if b_coords[1] < 0 or b_coords[3] >= Consts.HIGHT:
            return True
        return False  # Didn't passed the limits
