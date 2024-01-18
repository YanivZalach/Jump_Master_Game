# Imports Libraries
import time
import  random

# The gui engine
from tkinter import Label, Canvas, Button, Tk

# Local Libraries
from src.window import Window
from src.const import Consts
from src.game import Move

# The main function
def main():
    # Drawing the canvas
    window , canvas = Window.drowWindow()
    # Drawing the bird
    bird = Window.drowBird(canvas)
    # TODO: DRAWING THE WALLS
    # TODO: ADDING A SCORE COUNTER, WITH THE RECORD, REMEMBER FROM GAME TO GAME

    # Accepting user input
    window.bind("<space>", lambda e: Move.Jump())


    # The window main loop
    try:
        # TODO: UPDATING THE WALLS EVERY TIME THE BIRD GETS TO THE MIDDLE OF THE SCREEN
        while True and window:
            # Updating the window
            window.update()
            # Moving the bird
            Move.moveBird(canvas,bird)
            # Did we lost
            if Move.Limits(canvas,bird):
                # Stopping the game
                break
            # Frame rate
            time.sleep(Consts.FRAME_RATE)  

        print("You Lost")
        # TODO: ADDING A FUNCTION FOR OTHER GAME

    except Exception as e:
        if Consts.DEBUG:
            print("The Error: "+e.__str__())
    finally:
        print("Thaks for playing")

    window.mainloop()


if __name__ == "__main__":
    main()
