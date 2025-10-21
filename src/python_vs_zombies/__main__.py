import os
import time
import pywinstyles
from random import choice
from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk

def start_game():
    root = CTk()
    root.title("Python v.s Zombies")
    root.minsize(1024, 600)
    root.maxsize(1024, 600)
    # Load image bg
    base_dir= os.path.dirname(__file__)
    background_path= os.path.join(base_dir, "assets/images/background.png")
    image = PhotoImage(file=background_path)
    bg_image = CTkLabel(root, image=image, text="")
    bg_image.place(relheight=1, relwidth=1)

    # planting
    normal_font = CTkFont(family="arial bold", size=20)
    cells_column = ((335, 83), (414, 83), (497, 83), (572, 83), (661, 83), (740, 83), (815, 83), (892, 83), (972, 83))
    cells_row = ((254, 183), (254, 274), (254, 377), (254, 470), (254, 570))

    class Plant:
        def __init__(self, window, text):
            self.label = CTkLabel(window, text = text, fg_color = "green2", text_color = "black")
            self.damage = 40
        def plant_place(self, x_size, y_size):
            self.label.place(x= x_size, y=y_size)
        def take_damage(self, amount):
            self.damage -= amount
            if self.damage == 0 :
                    self.label.destroy()
                    return False
            if self.damage > 0 :
                self.label.configure(fg_color = 'red')
                time.sleep(1)
    class Sunflower(Plant):
        def __init__(self, window, text):
            super().__init__(window, text)
    class Bean(Plant):
        def __init__(self, window, text):
            super().__init__(window, text)
        def attack(self, x_ball, y_ball):
            self.start = x_ball
            self.moving = self.start
            ball = CTkLabel(root, text = "O", width = 12, height = 10)
            ball.place(x = self.start - 60, y = y_ball - 80) 
            outside = False
            def fire():
                nonlocal outside
                self.moving += 3
                print(self.moving)
                ball.place(x = self.moving, y = y_ball - 70)
                print(f"y = {y_ball}")
                root.after(100,fire)
                print("anjam")
                for widget in root.winfo_children():
                    if isinstance(widget, CTkLabel) and "zombie" in widget.cget("text").lower():
                        zx, zy = widget.winfo_x(),widget.winfo_y()
                        if zx - x_ball < 10 and zy - y_ball < 10:
                            widget.damaged()
            fire()
    class Defensive(Plant):
        def __init__(self, window, text):
            super().__init__(window, text)



    zombies_number = [(0, 183), (0, 274), (0, 377), (0, 470), (0, 570)]
    class Zombie:
        def __init__(self, window, text, garden):
            self.lebel = CTkLabel(window, text = text)
            self.garden = garden
            self.start = 1050
            self.moving = 4
            self.x_moving = self.start
        def spown(self, row):
            self.lebel.place(x = 1050, y = row[1] - 65)

        def move(self, row):
            self.x_moving -= self.moving
            # print(self.x_moving)
            self.lebel.place(x = self.x_moving, y = row[1] - 65) 
            row_index = zombies_number.index(tuple(row))
            zombies_number[row[0]] = self
            for plant in garden[row_index]:
                if plant is not None:
                    x_plant = garden[row_index].index(plant)                 
                    column_plant = cells_column[x_plant][0]
                    between = column_plant - self.x_moving
                    if between >= 10:
                        speed = self.attack(x_plant,row_index)
                        if speed == False:
                            time.sleep(2)
                            self.moving = 4
                        if speed:
                            self.moving = 0                
            root.after(100, self.move, row)
        def attack(self,x_plant,y_plant):
            enenmy = self.garden[y_plant][x_plant]
            alive = enenmy.take_damage(20)
            if alive == False:
                return False
        def damaged(self):
            self.lebel.destroy()
    
    # all blocks
    garden = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ]
    # zombies***
    # spown 
    row_zombie = list(choice(zombies_number))
    my_zom = Zombie(root, "zombie", garden)
    my_zom.spown(row_zombie)
    my_zom.move(row_zombie)


    

    # frame
    flower_menu = CTkFrame(root, height = 250, width = 100, bg_color = "white", fg_color= "burlywood3") 
    flower_menu.place(x = 50, y = 60)
    flower_menu.pack_propagate(False)
    # flower = Panel(flower_menu, "sunflower", "orange2", "black", [10, 10])
    btm_sunflower = CTkButton(flower_menu, text = "sunflower", fg_color = "orange2", text_color="black", width = 80, height = 40, command = lambda : btm_clicked(btm_sunflower, Sunflower(root, "sunflower")))
    btm_sunflower.place(x = 10, y = 10)
    btm_potato = CTkButton(flower_menu, text= "potato", fg_color = "orangered2", text_color="black", width = 80, height = 40, command = lambda : btm_clicked(btm_potato, Defensive(root, "potato")))
    btm_potato.place(x = 10, y = 55)
    btm_bean = CTkButton(flower_menu, text = "beans",fg_color = "springgreen2", text_color="black", width = 80, height = 40, command = lambda : btm_clicked(btm_bean, Bean(root, "bean")))
    btm_bean.place(x = 10, y = 100)
    btm_pepper = CTkButton(flower_menu, text ="pepper", fg_color = "firebrick2", text_color="black", width = 80, height = 40, command = lambda : btm_clicked(btm_pepper, Defensive(root, "pepper")))
    btm_pepper.place(x = 10, y = 145 )
    btm_list = [btm_sunflower, btm_potato, btm_bean, btm_pepper]
    flower = None
    clicked = True
    def btm_clicked(flower_btm, plant):
        nonlocal clicked
        nonlocal flower
        nonlocal row_zombie
        flower = plant
        clicked = False
        for btm in btm_list:
            if btm != flower_btm:
                btm.configure(state = "disabled")
        if clicked == False:
            bg_image.bind("<Button-1>", garden_clicked)
        else:
            print("you have to clicked one button")
        
    def garden_clicked(event):
        nonlocal flower
        nonlocal clicked
        print(f"Mouse pointer coordinates: X={event.x}, Y={event.y}")
        x_mouse, y_mouse = event.x, event.y
        for cell in cells_column:
            x_cell, y_cell = cell
            if x_cell > x_mouse:
                column = cells_column.index(cell)
                break
        else:
            print("you clicked out of garden")
        for cell in cells_row:
            x_cell, y_cell = cell
            if y_cell > y_mouse:
                row = cells_row.index(cell)
                break
        else:
            print("you clicked out of garden") 
        
        x_label = cells_column[column]
        y_lebel = cells_row[row]
        print(row, column)
        if garden[row][column] is None:
            flower.plant_place(x_label[0] - 60, y_lebel[1] - 70)
            print(clicked)
            garden[row][column] = flower
            for i in btm_list:
                i.configure(state = "abled")
        print(row_zombie,y_lebel)
        if y_lebel[1] == row_zombie[1]:
            try:
                flower.attack(x_label[0], y_lebel[1])
            except:
                print("this flower is defensive")

        clicked = True
        
    root.mainloop()

def start_game_pressed(window):
    window.destroy()
    start_game()

def main():
    # Main Window
    game_window = CTk()
    game_window.title('Python v.s Zombies')
    game_window.minsize(640, 480)
    game_window.maxsize(1024, 768)
    game_window.columnconfigure(0, weight=1)
    game_window.columnconfigure(1, weight=1)
    game_window.columnconfigure(2, weight=1)
    game_window.rowconfigure(0, weight=1)
    game_window.rowconfigure(1, weight=1)

    #font
    title_font = CTkFont(family="Time New Roman", size=50)
    normal_font = CTkFont(family="Time New Roman", size=20)

    # label
    game_title = CTkLabel(game_window, text="Python vs Zombies", font=title_font)
    game_title.grid(row=0, column=0, columnspan=3, sticky='nesw')

    # Buttons
    button_configurations = dict(width=160, height=160, font=normal_font)
    start_buttom = CTkButton(game_window, text="Start Game", **button_configurations, command=lambda: start_game_pressed(game_window))
    settings_buttom = CTkButton(game_window, text="Settings", **button_configurations)
    quit_buttom = CTkButton(game_window, text="Quit", command=game_window.destroy, **button_configurations)
    start_buttom.grid(row=1, column=0, sticky='n')
    settings_buttom.grid(row=1, column=1, sticky='n')
    quit_buttom.grid(row=1, column=2, sticky='n')

    game_window.mainloop()


if __name__ == "__main__":
    main()