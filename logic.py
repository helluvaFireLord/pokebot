from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.gen_i_red_blue = self.get_gen_i_red_blue()
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return 'https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru'
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    #Метод для возвращения поколения i красный-синий
#"versions"['versions']['generation-i']['red-blue']['front_default']
    def get_gen_i_red_blue(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['versions']['generation-i']['red-blue']['front_default'])
        else:
            return 'https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru'
 

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"



    # Метод класса для получения картинки покемона
    def show_gen_i_red_blue(self):
        return self.gen_i_red_blue
    

    def show_img(self):
        return self.img



