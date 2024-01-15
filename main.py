# Imports Libraries
import time
import  random

# The gui engine
from tkinter import Label, Canvas, Button, Tk

# Local Libraries
from src.window import Window
from src.const import Consts
from src.game import Move

# Running the game
run_game : bool = True

# The main function
def main():
    # Drawing the canvas
    window , canvas = Window.drowWindow()
    # Drawing the bird
    bird = Window.drowBird(canvas)

    # The window main loop
    try:
        while run_game and window:
            # Updating the window
            window.update()
            # Moving the bird
            Move.moveBird(canvas,bird)
            # Frame rate
            time.sleep(Consts.FRAME_RATE)  

    except Exception as e:
        if Consts.DEBUG:
            print("The Error: "+e.__str__())
    finally:
        print("Thaks for playing")

    window.mainloop()


if __name__ == "__main__":
    main()
