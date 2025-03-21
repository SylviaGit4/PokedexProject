import tkinter as tk
import requests as rq
import json
import pandas as pd
from urllib.request import urlopen
from PIL import ImageTk

def poke_search(entry):

    url = 'https://pokeapi.co/api/v2/pokemon/' + entry.lower()
    url_response = rq.get(url)

    if url_response.status_code == 200:
        print("Request successful.")
        pokemon_data = url_response.json()
        valid = True
        return (valid, pokemon_data)

    else:
        print(f"Error, URL response {url_response.status_code}")
        valid = False
        return(valid, f"Error: URL response {url_response.status_code}")


def poke_lookup(poke_data):
    info_window = tk.Toplevel()
    info_window.title("Pokemon Inf")

    info_window.columnconfigure(0, weight=1)
    info_window.columnconfigure(1, weight=1)
    info_window.columnconfigure(2, weight=1)

    # Data
    poke_id = (poke_data["id"])
    poke_name = (poke_data["name"]).title()                                                                     
    poke_type = [typ["type"]["name"] for typ in poke_data["types"]]

    if poke_id != 678:
        poke_sprite_url = poke_data["sprites"]['front_default']
        poke_sprite = urlopen(poke_sprite_url)
        poke_image = ImageTk.PhotoImage(data=poke_sprite.read())

    elif poke_id == 678:
        poke_sprite = "No Valid Sprite"



    frm_info_main = tk.Frame(
        master=info_window,
        bg="indian red",
        highlightbackground="grey27",
        highlightthickness=5,
    )

    frm_info_main.grid(row=0,column=0)


    sub_btn=tk.Button(
        master=frm_info_main,
        text = "Close", 
        command = info_window.destroy,
        bg="firebrick3",
        fg="white",
    )

    lbl_name = tk.Label(
        master=frm_info_main,
        text=f"Pokemon: {poke_name}",
        bg="indian red",
        fg="white",
        padx="5",
    )   

    lbl_id = tk.Label(
        master=frm_info_main,
        text=f"ID: {poke_id}",
        bg="indian red",
        fg="white",
        padx="5",
    )   

    lbl_type_one = tk.Label(
        master=frm_info_main,
        text=f"Type 1: {(poke_type[0]).title()}",
        bg="indian red",
        fg="white",
        padx="5",
    ) 

    if len(poke_type) > 1:
        lbl_type_two = tk.Label(
            master=frm_info_main,
            text=f"Type 2: {(poke_type[1]).title()}",
            bg="indian red",
            fg="white",
            padx="5",
        )    
    
    else:
        lbl_type_two = tk.Label(
            master=frm_info_main,
            text=f"Type 2: N/A",
            bg="indian red",
            fg="white",
            padx="5",
        )    
    
    if poke_id != 678:
        lbl_poke_sprite = tk.Label(
            master=frm_info_main,
            image = poke_image,
            bg="indian red",
        )

    elif poke_id == 678:
        lbl_poke_sprite = tk.Label(
            master=frm_info_main,
            text=poke_sprite,
            fg="White",
            bg="indian red",
        )


    sub_btn.grid(row=0,column=0, pady=3)
    lbl_name.grid(row=1,column=0)
    lbl_id.grid(row=1,column=1)
    lbl_poke_sprite.grid(row=2, column=0, columnspan=2)
    lbl_type_one.grid(row=3,column=0, columnspan=1)
    lbl_type_two.grid(row=4,column=0, columnspan=1)

    info_window.mainloop()


def type_search(entry):

    url = 'https://pokeapi.co/api/v2/type/' + entry
    url_response = rq.get(url)

    if url_response.status_code == 200:
        print("Request successful.")
        type_data = url_response.json()

    else:
        print(f"Error, URL response {url_response.status_code}")

    
    info_window = tk.Toplevel()
    info_window.title("Type Ten")

    info_window.columnconfigure(0, weight=1)
    info_window.columnconfigure(1, weight=1)
    info_window.columnconfigure(2, weight=1)

    # Data
    top_pokemon = []

    for i in range(0,11):                                                
        poke_data = (type_data["pokemon"][i])
        top_pokemon.append(poke_data["pokemon"]["name"])


    frm_info_main = tk.Frame(
        master=info_window,
        bg="indian red",
        highlightbackground="grey27",
        highlightthickness=5,
    )

    frm_info_main.grid(row=0,column=0)


    sub_btn=tk.Button(
        master=frm_info_main,
        text = "Close", 
        command = info_window.destroy,
        bg="firebrick3",
        fg="white",
    )

    sub_btn.grid(row=0,column=0, pady=3)

    for i in range(0,11):
        poke_name = tk.Label(
            master=frm_info_main,
            text=f"Pokemon {[i]}: {top_pokemon[i].title()}",
            bg="indian red",
            fg="white",
            padx="5",
        )   
        poke_name.grid(row=[i+1],column=0)

    info_window.mainloop()

def replace(party_value, uid, selected_poke):
    df = pd.read_csv("users.csv")

    df.loc[df["UID"] == uid, party_value] = selected_poke

    df.to_csv("users.csv", index=False)