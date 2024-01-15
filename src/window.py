# Creating a window

# The gui engine
from tkinter import Label, Canvas, Button, Tk

# The game consts
from .const import Consts

class Window:
    @staticmethod
    def drowWindow():
        # Drawing the window
        window = Tk()
        # In the BACKGROUND color
        window.config(background=Consts.BACKGROUND)
        # In the needed geometry
        window.geometry((str)(Consts.WIDTH) + "x" + (str)(Consts.HIGHT))



        # Creating the canvas
        canvas=Canvas(
                window,
                width=Consts.WIDTH,
                height=Consts.HIGHT,
                background=Consts.BACKGROUND,
                highlightbackground=Consts.WALL_COLOR  # Use highlightbackground for the border color
                )
        canvas.pack()

        return window, canvas

    @staticmethod
    def drowBird(canvas, coordinates = Consts.BIRD_START):  # The default is for the start of the game
        # Drawing the bird, in the BIRD_COLOR color
        bird_ball = canvas.create_oval(*coordinates, fill=Consts.BIRD_COLOR)
        return bird_ball

