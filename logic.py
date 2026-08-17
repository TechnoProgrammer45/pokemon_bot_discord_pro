import aiohttp
import random
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.power = random.randint(30, 60)
        self.hp = random.randint(200, 400)
      
        self.last_feed_time = datetime.now()

        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                else:
                    return "Pikachu"

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"Pokémon ismi: {self.name}\nPokémon gücü: {self.power}\nPokémon sağlığı: {self.hp}"

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['sprites']['front_default']
                else:
                    return None

    async def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = random.randint(1, 5)
            if chance == 1:
                return f"Sihirbaz Pokémon kalkan kullandı ve saldırıyı püskürttü!"

        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pokémon eğitmeni @{self.pokemon_trainer}, @{enemy.pokemon_trainer}'ne saldırdı!\n@{enemy.pokemon_trainer}'nin kalan sağlığı: {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Pokémon eğitmeni @{self.pokemon_trainer}, @{enemy.pokemon_trainer}'ni yendi!"

    async def feed(self, feed_interval=60):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += 20 # Standart iyileşme
            self.last_feed_time = current_time
            return f"Pokémon'un başarıyla beslendi ve sağlığı geri kazanıldı. Güncel HP: {self.hp}"
        else:
            # Erken çağrıldığında bir sonraki beslenme zamanını hesaplayıp mesaj olarak döndürür
            next_feed_time = self.last_feed_time + delta_time
            return f"Pokémonunuz henüz acıkmadı! Bir sonraki besleme zamanı: {next_feed_time.strftime('%H:%M:%S')}"


class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp = random.randint(300, 500)

    async def attack(self, enemy):
        return await super().attack(enemy)

    async def feed(self):
        # Varsayılan 60 saniye yerine, sihirbazlar 20 saniyede bir beslenebilir.
        return await super().feed(feed_interval=20)



class Fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.power = random.randint(50, 80)

    async def attack(self, enemy):
        super_power = random.randint(5, 15)
        self.power += super_power
        result = await super().attack(enemy)
        self.power -= super_power
        return result + f"\nDövüşçü Pokémon süper saldırı kullandı! Eklenen güç: {super_power}"

    async def feed(self, feed_interval=60):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += 60 # Normalden çok daha fazla sağlık artışı (60)
            self.last_feed_time = current_time
            return f"Dövüşçü Pokémon'un güçlü bir öğünle beslendi! Güncel HP: {self.hp}"
        else:
            next_feed_time = self.last_feed_time + delta_time
            return f"Dövüşçü Pokémonunuz henüz acıkmadı! Bir sonraki besleme zamanı: {next_feed_time.strftime('%H:%M:%S')}"
