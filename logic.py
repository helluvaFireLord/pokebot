from random import randint

import requests


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.power = randint(30, 60)
        self.hp = randint(200, 400)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f'''Имя твоего покеомона: {self.name}
Сила покемона: {self.power}
Здоровье покемона: {self.hp}
'''

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


    def atk(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return 'Покемон-волшебник применил щит в сражении'
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f'Сражение @{self.name} c @{enemy.name}'
        else:
            enemy.hp = 0
            return f'Победа @{self.name} над @{enemy.name}'


class Wizard(Pokemon):
    pass


class Fighter(Pokemon):
    def atk(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().atk(enemy)
        self.power -= super_power
        return result + f'\nБоец применил супер-атаку силой: {super_power}'
    

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.atk(wizard))