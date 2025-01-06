import requests

def fetch_pokemon_data(pokemon_name):
    # Funzione per recuperare i dati di un Pokémon tramite l'API di PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data
