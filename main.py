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

# Stopping the game
def on_closing(window):
    # This function will be called when the user tries to close the window
    global run_game
    run_game = False
    # give some time to stop the for loop before destroying window
    print("Window is closing. Performing cleanup or showing a message.")
    window.after(Consts.CLOSE_WINDOW, window.destroy())  # Close the window

# The main function
def main():
    # Drawing the canvas
    window , canvas = Window.drowWindow()
    # In the case of closing the window
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window))
    # Drawing the bird
    bird = Window.drowBird(canvas)

    # The window main loop
    try:
        while run_game:
            if window:
                # Updating the window
                window.update()
                # Moving the bird
                Move.moveBird(canvas,bird)
            # Frame rate
            time.sleep(Consts.FRAME_RATE)  

    except KeyboardInterrupt:
        print("Thaks for playing")

    window.mainloop()


if __name__ == "__main__":
    main()
