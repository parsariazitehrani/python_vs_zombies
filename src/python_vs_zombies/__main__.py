from customtkinter import *
from PIL import Image,ImageTk
import os

def start():
    levels = 0

    run_game = CTk()
    run_game.geometry('640x480')
    run_game.minsize(640, 480)
    run_game.maxsize(1024, 768)
    # grid
    run_game.columnconfigure(0, weight=1)
    run_game.columnconfigure(1, weight=1)
    run_game.columnconfigure(2, weight=1)
    run_game.columnconfigure(3, weight=1)
    run_game.columnconfigure(4, weight=1)
    run_game.columnconfigure(5, weight=1)
    run_game.columnconfigure(6, weight=1)
    run_game.columnconfigure(7, weight=1)
    run_game.columnconfigure(8, weight=1)
    run_game.rowconfigure(0, weight=1)
    run_game.rowconfigure(1, weight=1)
    run_game.rowconfigure(2, weight=1)
    run_game.rowconfigure(3, weight=1)
    run_game.rowconfigure(4, weight=1)
    run_game.rowconfigure(5, weight=1)
    # size
    noraml_button = dict(width=170, height=170, )
    progress = dict(width=190, height=20)
    normal_lable = CTkFont(family="Time New Roman", size=20)
    # lable
    lev = CTkLabel(run_game,text=f"level:{levels}", font=normal_lable)
    lev.grid(row= 0,column=0,sticky='nw')
    # import
    base_back= os.path.dirname(__file__)
    path_back= os.path.join(base_back, "assets", "images", "backgropund.png")
    back= Image.open(path_back).resize((200,200))
    ctk_back= CTkImage(light_image=back)
    # Image
    lable_back= CTkLabel(run_game, image=ctk_back, width=20, height=20,text='')
    lable_back.grid(row= 3, column= 3)
    # progress
    game_time = CTkProgressBar(run_game, orientation=HORIZONTAL, **progress)
    game_time.grid(row = 0, column=9, columnspan=3, sticky='n')

    for i in range(20):
        game_time.start()
        if i == 20 :
            game_time.stop()
    run_game.mainloop()

def quit_window(window):
    window.destroy()
def start_game(window):
    window.destroy()
    start()

def main():
    # Main Window
    main_window = CTk()
    main_window.title('Python v.s Zombies')
    main_window.geometry('640x480')
    main_window.minsize(640, 480)
    main_window.maxsize(1024, 768)
    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=1)
    main_window.columnconfigure(2, weight=1)
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=1)
    #font
    title_font = CTkFont(family="Time New Roman", size=50)
    normal_font = CTkFont(family="Time New Roman", size=20)
    # lable
    game_title = CTkLabel(main_window, text="Python vs Zombies", font=title_font)
    game_title.grid(row=0, column=0, columnspan=3, sticky='nesw')
    # Buttons
    button_configurations = dict(width=160, height=160, font=normal_font)
    start_buttom = CTkButton(main_window, text="Start Game", **button_configurations, command=lambda: start_game(main_window))
    settings_buttom = CTkButton(main_window, text="Settings", **button_configurations)
    quit_buttom = CTkButton(main_window, text="Quit", command=lambda: quit_window(main_window), **button_configurations)
    start_buttom.grid(row=1, column=0, sticky='n')
    settings_buttom.grid(row=1, column=1, sticky='n')
    quit_buttom.grid(row=1, column=2, sticky='n')

    main_window.mainloop()

if __name__ == '__main__':
    main()








#    ******** what is the problme???????*********