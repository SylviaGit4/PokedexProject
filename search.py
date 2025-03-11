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
        return(valid, f"Error, URL response {url_response.status_code}")