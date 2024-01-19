# Creating a window

# The gui engine
from tkinter import Label, Canvas, Tk

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
        window.geometry((str)(Consts.WIDTH) + "x" + (str)(Consts.HIGHT_WITH_LABAL))
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
    def drowScore(window,game_time:float,best_time:float):
        # Checking for the best time
        if best_time < game_time:
            best_time = game_time
        # Creating a label for the score
        score = Label(
                window,
                text=f"you lasted:{game_time:.3f} seconds \n your best: {best_time:.3f}",
                font=Consts.FONT,
                width=Consts.WIDTH_LABEL,
                height=Consts.HIGHT_LABEL,
                bg=Consts.LABEL_COLOR,
                fg=Consts.LABEL_TEXT_COLOR
                )
        score.pack()
        return score,best_time

    @staticmethod
    # Stopping the game
    def on_closing(window):
        # This function will be called when the user tries to close the window
        # give some time to stop the for loop before destroying window
        if Consts.DEBUG:  # Debugging mode
            print("Window is closing. Performing cleanup.")
        window.after(Consts.CLOSE_WINDOW, window.destroy())  # Close the window

