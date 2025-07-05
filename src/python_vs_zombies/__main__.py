import os
import time

from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk

def start_game():
    root = CTk()
    root.title("Python v.s Zombies")
    root.minsize(1024, 600)
    root.maxsize(1024, 600)
    # root.columnconfigure(0, weight=2)
    # root.columnconfigure(1, weight=3)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(3, weight=2)
    root.rowconfigure(4, weight=2)
    root.rowconfigure(5, weight=2)
    root.rowconfigure(6, weight=1)
    # Load image bg
    base_dir= os.path.dirname(__file__)
    background_path= os.path.join(base_dir, "assets/images/background.png")
    image = PhotoImage(file=background_path)
    bg_image = CTkLabel(root, image=image, text="")
    bg_image.place(relheight=1, relwidth=1)
    # test
    # plant1= CTkLabel(root, text="flower")
    # plant1.grid(row=2, column=2)
    # zobmei1= CTkLabel(root, text="zombie") 
    # zobmei1.grid(row=2, column= 11)
    def movement(root, label):
        move = 0
        for i in range(10):
            move += 1
            label.grid(row= 2, column= 10, padx= move, pady= 1, sticky="w")
            root.update()
            time.sleep(0.2)
    potato= CTkLabel(root, text="potato")
    potato.grid(row= 2, column= 1, padx= 15, pady= 60, sticky="e")
    btm = CTkButton(root, text="move!", command=lambda: movement(root, dadash))
    btm.grid(row = 7)
    dadash= CTkLabel(root, text="dada potato")
    dadash.grid(row= 2, column= 10, padx= 190, pady= 1, sticky="w")
    
    # point= CTkLabel(root, text="point:20")
    # point.grid(row=0, column=2)
    # timeline= CTkProgressBar(root)
    # timeline.grid(row= 0, column= 12)

    #its too long and mess up grid
    
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