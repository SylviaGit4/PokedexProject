import tkinter as tk
import requests as rq
import json
import login

########################
root = tk.Tk()
root.title("Pokedex")
########################

#Calling the login function later
def user_login():
    user_data = login.user_login()
    
    lbl_username.config(text=user_data[0])
########################

frm_main = tk.Frame(
    root,
    bg="SlateGray1",
    height="400",
    width="400",
    highlightbackground="grey27",
    highlightthickness=5,
    )


frm_key_right = tk.Frame(
    root,
    bg="indian red",
    height="600", 
    width="200", 
    padx="10",
    pady="5",
    )

frm_key_bottom = tk.Frame(
    root,
    bg="indian red",
    height="200",
    width="400", 
    )

frm_main.grid(column=0,row=0, rowspan=1, sticky="ns")
frm_key_right.grid(column=1, row=0, rowspan=2, sticky="ns")
frm_key_bottom.grid(column=0, row=1, sticky="ns")

btn_login = tk.Button(
    master=frm_key_right,
    text="Login",
    command=lambda:user_login(),
    bg="firebrick3",
    fg="white",
    padx="5",
)

lbl_username = tk.Label(
    master=frm_key_right,
    text="USERNAME",
    bg="firebrick3",
    fg="white",
    padx="5",
)

lbl_username.grid(column=0, row=0)
btn_login.grid(column=0, row=1)

########################
root.mainloop()
