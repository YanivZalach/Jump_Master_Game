# Creating a window

# The gui engine
from tkinter import Label, Canvas, Button, Tk

# The game consts
from .const import Consts, WALLS_START

class Window:
    @staticmethod
    def drowWindow():
        # Drawing the window
        window = Tk()
        # In the BACKGROUND color
        window.config(background=Consts.BACKGROUND)
        # In the needed geometry
        window.geometry((str)(Consts.WIDTH) + "x" + (str)(Consts.HIGHT))
        # In the case of closing the window
        window.protocol("WM_DELETE_WINDOW", lambda: Window.on_closing(window))



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

    @staticmethod
    def drowWalls(canvas, coordinates = WALLS_START):  # The default is for the start of the game
        # Drawing the Walls, in the WALL_COLOR color
        walls = []  # List of the 4 walls
        for wall_cords in coordinates:
            walls.append(canvas.create_rectangle(*wall_cords,fill=Consts.WALL_COLOR))
        return walls

    @staticmethod
    # Stopping the game
    def on_closing(window):
        # This function will be called when the user tries to close the window
        # give some time to stop the for loop before destroying window
        print("Window is closing. Performing cleanup.")
        window.after(Consts.CLOSE_WINDOW, window.destroy())  # Close the window

