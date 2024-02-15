# Imports Libraries
import time
from typing import List

# Local Libraries
from src.window import Window
from src.const import Consts
from src.game import Move

# The running game indicator
game_run = True
# Drawing the canvas
window , canvas = Window.drowWindow()
# Time counter
best_time:float = 0
# Drawing the score
score, best_time= Window.drowScore(window,0,0)

# Playing the game
def gameRun(window,canvas):
    global game_run, score, best_time
    # Drawing the bird
    bird = Window.drowBird(canvas)
    # Drawing the walls
    walls : List = Window.drowWalls(canvas)
    start_time = time.time()  # Starting the game counter
    while game_run and window:
        # Updating the window
        window.update()
        # Moving the bird
        Move.moveBird(canvas,bird)
        # Moving the walls
        walls : List = Move.toMoveWalles(canvas,walls,start_time)
        # Did we lost
        if Move.limits(canvas,bird,walls):
            # Stopping the game
            game_run = False
            break
        # Frame rate
        time.sleep(Consts.FRAME_RATE)  

    end_time = time.time()  # Ending the game counter
    game_time = end_time - start_time  # Calculating the game duration
    # Deleting all the assets
    canvas.delete(*walls)
    canvas.delete(bird)
    # Deleting last score, printing new one
    score.destroy()
    score,best_time = Window.drowScore(window,game_time,best_time)

# Making the game interactive using the space bar
def gamePress():
    global game_run
    if game_run:
        Move.jump()
    else:
        # Resetting the vars
        game_run = True
        Consts.VY = Consts.VY_O
        Consts.WALLS_SWITCH_STERT_L = Consts.WALLS_SWITCH_STERT_L_O
        Consts.WALLS_SWITCH_START_R = Consts.WALLS_SWITCH_START_R_O
        Consts.VX = Consts.VX_O
        # Starting a new game
        gameRun(window,canvas)

# The main function
def main():
    # Accepting user input
    window.bind("<space>", lambda _: gamePress())
    # The window main loop
    try:
        gameRun(window,canvas)
    except Exception as e:
        if Consts.DEBUG:  # Debugging mode
            print("The Error: "+e.__str__())

    window.mainloop()

# Calling the main function
if __name__ == "__main__":
    main()
