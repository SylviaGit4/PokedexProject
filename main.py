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
#login_valid, user_id = login.user_login("test","test")
#print(user_id)

########################
root.mainloop()