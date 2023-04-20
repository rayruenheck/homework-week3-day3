import requests
from IPython.display import Image

class Pokemon1():
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname
        self.abilities = []
        self.types = []
        self.weight = None
        self.image = None
        self.pokemon_image
   
    def pokemon_image(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        response.status_code
        if response.status_code == 200:
            print('success')
            data = response.json()
            self.image = data['sprites']['versions']['generation-i']['red-blue']['front_default']