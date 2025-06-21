from customtkinter import *
import tkinter.font as tkfont

def quit():
    main_win.destroy()
# windows
main_win = CTk()
main_win.maxsize(640,480)
main_win.minsize(640,480)
main_win.rowconfigure(1, weight=1)
main_win.columnconfigure(1, weight=0)
# font
title = CTkFont(family="Time New Roman",size=50)
normal_font = CTkFont(family="Time New Roman",size=20)
# lable
name_game = CTkLabel(main_win,text='python vs zombies',font=title)
name_game.place(x=120, y=45)
# button
star_buttom = CTkButton(main_win,font=normal_font ,text="start game",width=110, height=110,fg_color="sienna1",hover_color='coral1')
star_buttom.place(x=265, y=180)
settings_button = CTkButton(main_win,font=normal_font, text='settings',width=110, height=110,fg_color='palegreen3',hover_color='khaki3')
settings_button.place(x=80, y=180 )
quit_button = CTkButton(main_win,text="quit",command=quit,font=normal_font,width=110,height=110,fg_color='turquoise3',hover_color='darkseagreen4')
quit_button.place(x=450,y=180)


main_win.mainloop()