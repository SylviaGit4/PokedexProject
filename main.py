import tkinter as tk
import requests as rq
import json
import login

########################
root = tk.Tk()
root.title("Pokedex")
root.geometry("600x800")
########################

#Calling the login function later
def user_login():
    user_id = login.user_login()
    print(user_id)
########################

frm_main = tk.Frame(
    root,
    bg="SlateGray1",
    height="400px",
    width="400px",
    highlightbackground="grey27",
    highlightthickness=5,
    )
frm_main.grid(column=0,row=0, rowspan=1)


frm_key_right = tk.Frame(
    root,
    bg="indian red",
    height="600px", 
    width="100px", 
    )
frm_key_right.grid(column=1, row=0, rowspan=2)

frm_key_bottom = tk.Frame(
    root,
    bg="indian red",
    height="200px",
    width="400px", 
    )
frm_key_bottom.grid(column=0, row=1)


btn_login = tk.Button(
    master=frm_key_right,
    text="Login",
    command=user_login,
    bg="white",
)
btn_login.grid(column=0, row=0)

########################
root.mainloop()
