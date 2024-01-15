# The gui engine
from tkinter import Canvas, Tk

# The game consts
from .const import Consts

# Function that move the game
class Move:
    # Function to move the bird
    @staticmethod
    def moveBird(canvas,bird):
        canvas.move(bird, Consts.VX, Consts.VY)

