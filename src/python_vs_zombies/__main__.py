from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
import os


def start_game():
    root = CTk()
    root.title("Python v.s Zombies")
    root.minsize(640, 480)
    root.maxsize(1024, 768)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # Load image
    base_dir= os.path.dirname(__file__)
    background_path= os.path.join(base_dir, "assets/images/background.png")
    image = PhotoImage(file=background_path)
    bg_image = Label(root, image=image)
    bg_image.place(relheight=1, relwidth=1)

    label_col_0 = CTkLabel(root, text="1")
    label_col_1 = CTkLabel(root, text="0")
    label_col_2 = CTkLabel(root, text="0")
    label_col_0.grid(row=0, column=0)
    label_col_1.grid(row=0, column=1)
    label_col_2.grid(row=0, column=2)
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