import discord
from discord.ext import commands
from config import token
from logic import Pokemon, Wizard, Fighter
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Giriş yapıldı: {bot.user.name}')

@bot.command()
async def go(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons:
        chance = random.randint(1, 5)
        if chance <= 3:
            pokemon = Pokemon(author)
        elif chance == 4:
            pokemon = Wizard(author)
        else:
            pokemon = Fighter(author)

        await ctx.send(await pokemon.info())
        image_url = await pokemon.show_img()
        if image_url:
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Pokémon görüntüsü yüklenemedi.")
    else:
        await ctx.send("Zaten bir Pokémon oluşturmuşsun.")

@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None
    if target:
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy = Pokemon.pokemons[target.name]
            attacker = Pokemon.pokemons[ctx.author.name]

            if attacker.hp <= 0:
                await ctx.send("Pokémon'unun canı bitmiş! Dövüşebilmek için önce `!feed` komutunu kullan.")
                return

            result = await attacker.attack(enemy)
            await ctx.send(result)
        else:
            await ctx.send("Savaş için her iki tarafın da bir Pokémon'a sahip olması gerekir!")
    else:
        await ctx.send("Saldırmak istediğiniz kullanıcıyı etiketleyin. Örn: !attack @Kullanıcı")

@bot.command()
async def feed(ctx):
    author = ctx.author.name
    # Kullanıcının sözlükte kayıtlı bir pokémonu olup olmadığını kontrol ediyoruz
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        # logic.py dosyasındaki yazdığımız feed() metodunu çağırıp mesajı alıyoruz
        result_message = await pokemon.feed()
        # Oyuncuya bot üzerinden durumu bildiriyoruz
        await ctx.send(result_message)
    else:
        await ctx.send("Henüz besleyecek bir Pokémon'un yok! `!go` yazarak bir tane oluşturabilirsin.")

bot.run(token)
