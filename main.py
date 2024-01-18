# Imports Libraries
import time
import  random

# The gui engine
from tkinter import Label, Canvas, Button, Tk
from typing import List

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
    # Drawing the walls
    walls : List = Window.drowWalls(canvas)
    # TODO: ADDING A SCORE COUNTER, WITH THE RECORD, REMEMBER FROM GAME TO GAME

    # Accepting user input
    window.bind("<space>", lambda e: Move.Jump())


    # The window main loop
    try:
        # TODO: UPDATING THE WALLS EVERY TIME THE BIRD GETS TO THE MIDDLE OF THE SCREEN
        start_time = time.time()  # Starting the game counter
        while True and window:
            # Updating the window
            window.update()
            # Moving the bird
            Move.moveBird(canvas,bird)
            # Moving the walls
            walls : List = Move.toMoveWalles(canvas,walls,start_time)
            # Did we lost
            if Move.Limits(canvas,bird):
                # Stopping the game
                break
            # Frame rate
            time.sleep(Consts.FRAME_RATE)  

        end_time = time.time()  # Ending the game counter
        game_time = end_time - start_time  # Calculating the game duration
        print("You Lost ",game_time)
        # TODO: ADDING A FUNCTION FOR OTHER GAME
    except Exception as e:
        if Consts.DEBUG:
            print("The Error: "+e.__str__())

    finally:
        print("Thaks for playing")

    window.mainloop()


if __name__ == "__main__":
    main()
