import tkinter as tk
import requests as rq
import json
import login
import data

########################
root = tk.Tk()
root.title("Pokedex")
########################

### EXTERNAL FUNCTIONS & NECESSARY DEFINITIONS
global search_response

search_response = ""

all_types = [
 "normal", "fire", "water", "grass", "flying", "fighting",
 "poison", "electric", "ground", "rock", "psychic", "ice", 
 "bug", "ghost", "steel", "dragon", "dark", "fairy"
 ]

# Login Function
def login_button():
    user_data = login.user_login()
    print(user_data)
    #lbl_username.config(text="username")

# Search Function
def search_button(entry):
    entry = entry.lower()

    global search_response ## DO NOT DELETE THIS, IT WILL BREAK IF YOU DO.

    if entry == "":
        lbl_error_handle.config(text="Error: No Input")

    else: 
        if entry in all_types:
            data.type_search(entry)

        else:
            valid, search_response = data.poke_search(entry)

            if valid == True:
                poke_name = (search_response['name']).title()
                lbl_pokemon_name.config(text=f"Selected Pokemon: {poke_name}")
                lbl_error_handle.config(text="No Error Detected")
            
            else:
                lbl_pokemon_name.config(text="Selected Pokemon: N/A")
                lbl_error_handle.config(text=search_response)

# Pokemon Info Function
def poke_info(entry):
    if lbl_error_handle.cget("text") == "No Error Detected":
        data.poke_lookup(entry)

    else:
        print("No valid data.")
        lbl_error_handle.config(text="Error: No Valid Data")

########################

frm_main = tk.Frame(
    root,
    bg="SlateGray1",
    height="400",
    width="400",
    highlightbackground="grey27",
    highlightthickness=5,
    padx="10",
    pady="5",
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

frm_main.grid(column=0, row=0, rowspan=1, sticky="nsew")
frm_key_right.grid(column=1, row=0, rowspan=2, sticky="nsew")
frm_key_bottom.grid(column=0, row=1, rowspan=1, sticky="nsew")

## RIGHT SIDE STUFF
btn_login = tk.Button(
    master=frm_key_right,
    text="Login",
    command=lambda:login_button(),
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

lbl_username.grid(column=0, row=0, pady="2")
btn_login.grid(column=0, row=1, pady="2")

## MAIN STUFF

lbl_search = tk.Label(
    master=frm_main,
    text="Input Pokemon Name/ID:",
    bg="SlateGray1",
    fg="black",
)

search_entry = tk.Entry(
    master=frm_main,
    bg="SlateGray2",
    fg="black",
)

btn_search = tk.Button(
    master=frm_main,
    text="SEARCH",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: search_button(search_entry.get()),
)

lbl_pokemon_name = tk.Label(
    master=frm_main,
    text="Selected Pokemon: N/A",
    bg="SlateGray2",
    fg="black",
    highlightbackground="grey21",
    highlightthickness=2,
)

lbl_error_handle = tk.Label(
    master=frm_main,
    text="No Error Detected",
    bg="SlateGray2",
    fg="black",
    highlightbackground="grey21",
    highlightthickness=2,
)

btn_info = tk.Button(
    master=frm_main,
    text="POKE-INFO",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: poke_info(search_response),
)

lbl_search.grid(column=0,row=0, columnspan=1)
search_entry.grid(column=0, row=1)
btn_search.grid(column=1, row=1, padx=2)
btn_info.grid(column=2, row=1, padx=2)
lbl_pokemon_name.grid(column=0,row=2, columnspan=1, padx=2, pady=2)
lbl_error_handle.grid(column=1,row=2, columnspan=2, padx=2, pady=2)


########################
root.mainloop()
