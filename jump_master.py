#liberis
import time
from  tkinter import *
import  random
import numpy as np

def reset_time():
    with open("score.txt", "w") as f:
        # Read the contents of the file into a string
        f.write("[0.0]")

def add_text(run_time_):
    now,best=add_score(run_time_)
    score = Label(window, text=f"you lasted:{now:.3f} seconds \n your best: {best:.3f}", font=('david', 40), width=20, height=2, bg='white', fg='black')
    score.place(x=80, y=470)

def add_score(new_score):
    # Open the file for reading
    with open("score.txt", "r") as f:
        # Read the contents of the file into a string
        contents = f.read()

        # Use the eval() function to convert the string to a list
        my_list = eval(contents)

    # Append a number to the list
    my_list.append(new_score)

    # Open the file for writing
    with open("score.txt", "w") as f:
        # Write the updated list back to the file
        f.write(str(my_list))
    return new_score,np.max(my_list)


def display_message(message):
    # Create a label widget to display the message
    label =Label(window, text=message, font=('david', 40), width=15, height=4, bg='red', fg='black')
    label.place(x=80,y=100)

    # Schedule the message to be destroyed after 3 seconds
    window.after(700, label.destroy)
def play_game():
    # Call the display_message function with a custom message
    display_message("You lost!\nLet's play to win")

def change_wall(origem,lefts):
     num=random.randrange(0,np.round(HIGHT / ( bull_dimeter*2)))
     num=np.round(num)
     change_=origem
     if(random.choice([True,False])):

             change_-=-num+change_
     else:
             change_+=change_+num

     if(change_<HIGHT*0.2):
         change_=HIGHT*0.2
     elif change_>HIGHT*0.8:
         change_=HIGHT*0.8
     if(lefts):
        return create_walls( change_,origem)#chainging the walss to a random place
     return  create_walls(origem,change_)  # chainging the walss to a random place

def Jump1():#the small jump
        for i in range(2*add):
                move_(vx,vy,True)
def Jump2():#the big jump
        for i in range(5*add):
                move_(vx,vy,True)
def Jump3():  # the ultra big jump
        for i in range(8 * add):
            move_(vx, vy*3, True)

def bed_cirdinets():#the walls cordinats
        c1 = canvas.coords(wall1)
        c2 = canvas.coords(wall2)
        c3 = canvas.coords(wall3)
        c4 = canvas.coords(wall4)
        list=[]
        for i in range(4):
                list.append((c1[i],c2[i],c3[i],c4[i]))
        return list

def move_(vx,vy,change_vy=False):#the mane -the fanction that is moving the ball
        codinats=canvas.coords(bird_ball)#cord of the bird
        wall_cordinets=bed_cirdinets()#cord of walls
        run=True#the indicator the program is runing
        if codinats[0]<0 or codinats[2]>=WIDTH:#no leting the bird to go out of bound
                vx= -vx
        if codinats[1] <= 0 or codinats[3] >= HIGHT_work:#stoping the game if the bird is tucing the flor or siling
                run=False
        #stoping the program if the bird tuched the wall(no meter witch one
        elif codinats[0]<wall_cordinets[2][0] and(codinats[1]<wall_cordinets[3][0] or codinats[3]>wall_cordinets[1][1]):
                run=False
        elif codinats[2]>wall_cordinets[0][2] and(codinats[1]<wall_cordinets[3][2] or codinats[3]>wall_cordinets[1][3]):
                run=False
        if change_vy:#movment while the jump buten(no meter witch on) had beem presd
                canvas.move(bird_ball, vx, -vy)

        else:#the reguler movment
                canvas.move(bird_ball,vx,vy)
        return vx,vy,run

def create_walls(start_hight_walls_l,start_hight_walls_r):
        # creating wall
        wall1 = canvas.create_rectangle(0, 0, width_walls, start_hight_walls_l - bull_dimeter * 3 - 1,
                                        fill="black")  # high left wall
        wall2 = canvas.create_rectangle(0, start_hight_walls_l + bull_dimeter * 3 + 1, width_walls, HIGHT_work,
                                        fill="black")  # low left wall

        wall3 = canvas.create_rectangle(WIDTH - width_walls, 0, WIDTH, start_hight_walls_r - bull_dimeter * 3 - 1,
                                        fill="black")  # high right wall
        wall4 = canvas.create_rectangle(WIDTH - width_walls, start_hight_walls_r + bull_dimeter * 3 + 1, WIDTH,
                                        HIGHT_work, fill="black")  # low right wall
        return wall1,wall2,wall3,wall4


reset_time()
window=Tk()
window.config(background="green")
#window.config(background='red')
#static valuse
#spce of work
WIDTH=400
HIGHT=400
HIGHT_work=450
#the moving bull valosites
vy=1
vx=2
#the jump value
add = 10
#the daimeter of the ball
bull_dimeter=15
#the bird cordinats
start_x_y=[0,200]
#the bird cordinats as the code get them
start_cord=[start_x_y[0],start_x_y[1]-bull_dimeter/2,start_x_y[0]+bull_dimeter,start_x_y[1]+bull_dimeter/2]
#the width of the walls
width_walls=20
#the place where there are no walls at first-the place of the bird
start_hight_walls=start_x_y[1]

geomtry_=(str)(WIDTH*2)+"x"+(str)(HIGHT+200)

window.geometry(geomtry_)



canvas=Canvas(window,width=WIDTH,height=HIGHT_work,background="#FFFF12")#work canvas
jump_button1=Button(window,font=('david',40),text='Jump low',command=Jump1,height=1,width=10,
                    background='#0012FF',activebackground='green')#Jump Buuten-low jamp
jump_button2=Button(window,font=('david',40),text='Jump high',command=Jump2,height=1,width=10,
                    background='#FF3344',activebackground='green')#Jump Buuten-high jump
jump_button3=Button(window,font=('david',40),text='ULTRA Jump',command=Jump3,height=1,width=10,
                    background='#00AA00',activebackground='green')#Jump Buuten-high ultra jump
_score=add_text(0.0)

#creating the canvas
canvas.place(x=0,y=0)
#creating the buutens
jump_button1.place(x=WIDTH+20,y=10)
jump_button2.place(x=WIDTH+20,y=130)
jump_button3.place(x=WIDTH+20,y=250)

window.bind("a", lambda event: Jump1())
window.bind("s", lambda event: Jump2())
window.bind("d", lambda event: Jump3())


to_run = True
while to_run:
    bird_ball = canvas.create_oval(start_cord[0], start_cord[1], start_cord[2], start_cord[3],
                                   fill="red")  # the moving ball

    wall1, wall2, wall3, wall4 = create_walls(start_hight_walls, start_hight_walls)
    #the indicatur the program is runing
    runing=True
    #the starting time of the program
    start_time=time.time()
    run_time=time.time()-start_time#the time our program ran
    #the actoual runing program
    while runing:
            #updating ouer walues of moving
            vx,vy,runing=move_(vx,vy)
            window.update()#refrash the game
            run_time = time.time() - start_time  # the time our program ran
            if (canvas.coords(bird_ball)[0]+canvas.coords(bird_ball)[2])/2<WIDTH*0.02 :
                origen = (canvas.coords(wall1)[3])+bull_dimeter*3+1
                canvas.delete(wall1, wall2, wall3, wall4)
                wall1, wall2, wall3, wall4 = change_wall(origen,False)
            #if(np.floor(run_time*1000)%2500>0 and np.floor(run_time*1000)%2500<35 and run_time>1):#chainging the walls place
            elif (canvas.coords(bird_ball)[0]+canvas.coords(bird_ball)[2])/2 >WIDTH*0.98:
                    origen = (canvas.coords(wall3)[3])+bull_dimeter*3+1
                    canvas.delete(wall1,wall2,wall3,wall4)
                    wall1,wall2,wall3,wall4=change_wall(origen,True)
            time.sleep(0.01)#the stop betwin the frams
    _score=add_text(run_time)
    print(f"you lasted: {run_time:.3f} seconds")#printing the result-the score
    play_game()
    window.update()#refrash the game
    canvas.delete(wall1, wall2, wall3, wall4,bird_ball)
     # the stop betwin the frams
    time.sleep(0.7)

    #canvas.itemconfigure(bird_ball,fill='black')
window.mainloop()