import tkinter as tk
import requests as rq
import json

def poke_search(entry):

    url = 'https://pokeapi.co/api/v2/pokemon/' + entry
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
    info_window = tk.Tk()
    info_window.title("Pokemon Inf")
    info_window.geometry("200x100")

    info_window.columnconfigure(0, weight=1)
    info_window.columnconfigure(1, weight=1)
    info_window.columnconfigure(2, weight=1)

    # Data
    poke_name = (poke_data['name']).title()


    frm_main = tk.Frame(
        master=info_window,
        bg="indian red",
        height=75,
        width=200,
        highlightbackground="grey27",
        highlightthickness=5,
    )

    frm_main.grid(row=0,column=0)


    sub_btn=tk.Button(
        master=frm_main,
        text = "Close", 
        command = info_window.destroy(),
        bg="indian red",
        fg="white",
    )


    sub_btn.grid(row=3,column=1)

    info_window.mainloop()
