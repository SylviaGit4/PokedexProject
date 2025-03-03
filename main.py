import tkinter as tk
import requests as rq
import json
import login

########################
root = tk.Tk()
root.title("Pokedex")
root.geometry("480x680")
########################

#Calling the login function later
def user_login():
    user_id = login.user_login()
    print(user_id)
########################

frm_main = tk.Frame(
    bg="SlateGray1",
    height="400px",
    width="400px",
    highlightbackground="grey27",
    highlightthickness=5,
    )
frm_main.grid(column=0,row=0, rowspan=1)


frm_key_right = tk.Frame(
    bg="indian red",
    height="600px", 
    width="100px", 
    )
frm_key_right.grid(column=1, row=0, rowspan=2)

frm_key_bottom = tk.Frame(
    bg="indian red",
    height="200px",
    width="400px", 
    )
frm_key_bottom.grid(column=0, row=1)


btn_login = tk.Button(
    frm_main,
    text="Login",
    command=user_login,
    bg="white",
    master=frm_key_right,
)
btn_login.grid(column=0, row=1)

########################
root.mainloop()
