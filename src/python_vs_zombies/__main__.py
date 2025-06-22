from customtkinter import *
# import tkinter.font as tkfont


def quit_window(window):
    window.destroy()

def main():
    # Main Window
    main_window = CTk()
    main_window.title('Python v.s Zombies')
    main_window.geometry('640x480')
    main_window.minsize(640, 480)
    main_window.maxsize(1024, 768)

    #            column=0      column=1        column=2
    #        ┌─────────────┬──────────────┬────────────────┐
    #        │             │              │                │
    # row=0  │             │              │                │
    #        │             │              │                │
    #        ┼─────────────┼──────────────┼────────────────┼
    #        │             │              │                │
    # row=1  │             │              │                │
    #        │             │              │                │
    #        └─────────────┴──────────────┴────────────────┘
    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=1)
    main_window.columnconfigure(2, weight=1)
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=1)


    # Title
    #            column=0      column=1        column=2
    #        ┌─────────────┬──────────────┬────────────────┐
    #        │ [ ----------------------------------------] │ <----------------- columnspan=3
    # row=0  │ [ ---------PYTHON V.S ZOMBIES ------------] │ <- Stick to ('n' ) north, ('e') east, ('s') south, ('w') west
    #        │ [ ----------------------------------------] │             (Top, Right, Bottom, Left)
    #        ┼─────────────┼──────────────┼────────────────┼
    #        │             │              │                │
    # row=1  │             │              │                │
    #        │             │              │                │
    #        └─────────────┴──────────────┴────────────────┘
    title_font = CTkFont(family="Time New Roman", size=50)
    game_title = CTkLabel(main_window, text="Python vs Zombies", font=title_font)
    game_title.grid(row=0, column=0, columnspan=3, sticky='nesw')

    # Buttons
    normal_font = CTkFont(family="Time New Roman", size=20)
    button_configurations = dict(width=160, height=160, font=normal_font)
    star_buttom = CTkButton(main_window, text="Start Game", **button_configurations)
    settings_buttom = CTkButton(main_window, text="Settings", **button_configurations)
    quit_buttom = CTkButton(main_window, text="Quit", command=lambda: quit_window(main_window), **button_configurations)

    # Grid
    #            column=0      column=1        column=2
    #        ┌─────────────┬──────────────┬────────────────┐
    #        │ [ ----------------------------------------] │
    # row=0  │ [ ---------PYTHON V.S ZOMBIES ------------] │
    #        │ [ ----------------------------------------] │
    #        ┼─────────────┼──────────────┼────────────────┼
    # row=1  │[ START GAME]│[--SETTINGS--]│[------QUIT----]│ <- Stick to ('n') north or Top
    #        │             │              │                │
    #        │             │              │                │
    #        └─────────────┴──────────────┴────────────────┘
    star_buttom.grid(row=1, column=0, sticky='n')
    settings_buttom.grid(row=1, column=1, sticky='n')
    quit_buttom.grid(row=1, column=2, sticky='n')

    # Run
    main_window.mainloop()

if __name__ == '__main__':
    main()