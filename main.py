import tkinter as tk
import requests as rq
import json
import login
import poke_data
import pandas as pd


## LOG IN WINDOW
global user_id

user_id = login.login_view()

df = pd.read_csv("users.csv")
user_data =  df.loc[df["UID"] == user_id]

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

# Search Function
def search_button(entry):
    entry = entry.lower()

    global search_response ## DO NOT DELETE THIS, IT WILL BREAK IF YOU DO.
    global poke_name

    if entry == "":
        lbl_error_handle.config(text="Error: No Input")

    else: 
        if entry in all_types:
            poke_data.type_search(entry)

        else:
            valid, search_response = poke_data.poke_search(entry)

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
       poke_data.poke_lookup(entry)

    else:
        print("No valid data.")
        lbl_error_handle.config(text="Error: No Valid Data")

# Replace Pokemon
def replace_poke(label_num, party_value):
    poke_data.replace(party_value, user_id, poke_name)

    if label_num == "1":
        lbl_poke_name_one.config(text=poke_name)
    if label_num == "2":
        lbl_poke_name_two.config(text=poke_name)
    if label_num == "3":
        lbl_poke_name_three.config(text=poke_name)
    if label_num == "4":
        lbl_poke_name_four.config(text=poke_name)
    if label_num == "5":
        lbl_poke_name_five.config(text=poke_name)
    if label_num == "6":
        lbl_poke_name_six.config(text=poke_name)

# Options menu
def options(user_id):
    login.user_options(user_id)
    lbl_username.config(text=user_data.iloc[0,1])

# Party Pokemon Info
def selected_poke_info(poke_name):
    entry = poke_name.lower()

    if entry == "":
        lbl_error_handle.config(text="Error: No Input")

    else:
        valid, search_response = poke_data.poke_search(entry)

        if valid == True:
            lbl_error_handle.config(text="No Error Detected")

            poke_data.poke_lookup(search_response)

        else:
            lbl_error_handle.config(text=search_response)

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
    height="50",
    width="400", 
    )

frm_main.grid(column=0, row=0, rowspan=1, sticky="nsew")
frm_key_right.grid(column=1, row=0, rowspan=2, sticky="nsew")
frm_key_bottom.grid(column=0, row=1, rowspan=1, sticky="nsew")

# RIGHT SIDE STUFF
btn_close = tk.Button(
    master=frm_key_right,
    text="Close",
    command=root.destroy,
    bg="firebrick3",
    fg="white",
    padx="5",
)

lbl_username = tk.Label(
    master=frm_key_right,
    text=user_data.iloc[0,1],
    bg="firebrick3",
    fg="white",
    padx="5",
)

btn_options = tk.Button(
    master=frm_key_right,
    text="Options",
    command=lambda: options(user_id),
    bg="firebrick3",
    fg="white",
    padx="2",
)

lbl_username.grid(column=0, row=0, pady="2")
btn_close.grid(column=0, row=1, pady="2")
btn_options.grid(column=0, row=2, pady="2")

## MAIN STUFF

lbl_search = tk.Label(
    master=frm_main,
    text="Input Pokemon Name/ID/Type:",
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
    bg="thistle",
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


## POKEMON LIST
lbl_poke_one = tk.Label(
    master=frm_main,
    text=(f"Pokémon:"),
    bg="SlateGray1",
    fg="black",
)

lbl_poke_name_one = tk.Label(
    master=frm_main,
    text=(f"{user_data.iloc[0,3]}"),
    bg="SlateGray1",
    fg="black",
)

btn_poke_one = tk.Button(
    master=frm_main,
    text="Replace Selected",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: replace_poke("1", "Poke1"),
)

btn_info_one = tk.Button(
    master=frm_main,
    text="Info",
    bg="SlateGray2",
    fg="black",
    padx="2",
    command= lambda: selected_poke_info(lbl_poke_name_one.cget("text")),
)


lbl_poke_two = tk.Label(
    master=frm_main,
    text=(f"Pokémon:"),
    bg="SlateGray1",
    fg="black",
)

lbl_poke_name_two = tk.Label(
    master=frm_main,
    text=(f" {user_data.iloc[0,4]}"),
    bg="SlateGray1",
    fg="black",
)

btn_poke_two = tk.Button(
    master=frm_main,
    text="Replace Selected",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: replace_poke("2", "Poke2"),
)

btn_info_two = tk.Button(
    master=frm_main,
    text="Info",
    bg="SlateGray2",
    fg="black",
    padx="2",
    command= lambda: selected_poke_info(lbl_poke_name_two.cget("text")),
)


lbl_poke_three = tk.Label(
    master=frm_main,
    text=(f"Pokémon:"),
    bg="SlateGray1",
    fg="black",
)

lbl_poke_name_three = tk.Label(
    master=frm_main,
    text=(f" {user_data.iloc[0,5]}"),
    bg="SlateGray1",
    fg="black",
)

btn_poke_three = tk.Button(
    master=frm_main,
    text="Replace Selected",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: replace_poke("3", "Poke3"),
)

btn_info_three = tk.Button(
    master=frm_main,
    text="Info",
    bg="SlateGray2",
    fg="black",
    padx="2",
    command= lambda: selected_poke_info(lbl_poke_name_three.cget("text")),
)


lbl_poke_four = tk.Label(
    master=frm_main,
    text=(f"Pokémon:"),
    bg="SlateGray1",
    fg="black",
)

lbl_poke_name_four = tk.Label(
    master=frm_main,
    text=(f" {user_data.iloc[0,6]}"),
    bg="SlateGray1",
    fg="black",
)

btn_poke_four = tk.Button(
    master=frm_main,
    text="Replace Selected",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: replace_poke("4", "Poke4"),
)

btn_info_four = tk.Button(
    master=frm_main,
    text="Info",
    bg="SlateGray2",
    fg="black",
    padx="2",
    command= lambda: selected_poke_info(lbl_poke_name_four.cget("text")),
)


lbl_poke_five = tk.Label(
    master=frm_main,
    text=(f"Pokémon:"),
    bg="SlateGray1",
    fg="black",
)

lbl_poke_name_five = tk.Label(
    master=frm_main,
    text=(f" {user_data.iloc[0,7]}"),
    bg="SlateGray1",
    fg="black",
)

btn_poke_five = tk.Button(
    master=frm_main,
    text="Replace Selected",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: replace_poke("5", "Poke5"),
)

btn_info_five = tk.Button(
    master=frm_main,
    text="Info",
    bg="SlateGray2",
    fg="black",
    padx="2",
    command= lambda: selected_poke_info(lbl_poke_name_five.cget("text")),
)


lbl_poke_six = tk.Label(
    master=frm_main,
    text=(f"Pokémon:"),
    bg="SlateGray1",
    fg="black",
)

lbl_poke_name_six = tk.Label(
    master=frm_main,
    text=(f" {user_data.iloc[0,8]}"),
    bg="SlateGray1",
    fg="black",
)

btn_poke_six = tk.Button(
    master=frm_main,
    text="Replace Selected",
    bg="SlateGray2",
    fg="black",
    padx="5",
    command= lambda: replace_poke("6", "Poke6"),
)

btn_info_six = tk.Button(
    master=frm_main,
    text="Info",
    bg="SlateGray2",
    fg="black",
    padx="2",
    command= lambda: selected_poke_info(lbl_poke_name_six.cget("text")),
)


lbl_poke_one.grid(column=0,row=3, pady=2)
lbl_poke_name_one.grid(column=1,row=3, pady=2)
btn_poke_one.grid(column=2, row=3, pady=2)
btn_info_one.grid(column=3, row=3, pady=2, padx=2)

lbl_poke_two.grid(column=0,row=4, pady=2)
lbl_poke_name_two.grid(column=1,row=4, pady=2)
btn_poke_two.grid(column=2, row=4, pady=2)
btn_info_two.grid(column=3, row=4, pady=2, padx=2)

lbl_poke_three.grid(column=0,row=5, pady=2)
lbl_poke_name_three.grid(column=1,row=5, pady=2)
btn_poke_three.grid(column=2, row=5, pady=2)
btn_info_three.grid(column=3, row=5, pady=2, padx=2)

lbl_poke_four.grid(column=0,row=6, pady=2)
lbl_poke_name_four.grid(column=1,row=6, pady=2)
btn_poke_four.grid(column=2, row=6, pady=2)
btn_info_four.grid(column=3, row=6, pady=2, padx=2)

lbl_poke_five.grid(column=0,row=7, pady=2)
lbl_poke_name_five.grid(column=1,row=7, pady=2)
btn_poke_five.grid(column=2, row=7, pady=2)
btn_info_five.grid(column=3, row=7, pady=2, padx=2)

lbl_poke_six.grid(column=0,row=8, pady=2)
lbl_poke_name_six.grid(column=1,row=8, pady=2)
btn_poke_six.grid(column=2, row=8, pady=2)
btn_info_six.grid(column=3, row=8, pady=2, padx=2)

########################
root.mainloop()
