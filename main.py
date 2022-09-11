import csv
from random import randint
from textwrap import fill

import discord
from discord import app_commands

genres_1 = ['Comedy', 'Sports', 'Drama', 'School', 'Shounen', 'Music',
            'Romance', 'Sci-Fi', 'Adventure', 'Mystery', 'Fantasy', 'Action',
            'Military', 'Magic',  'Slice of Life', 'Psychological', 'Ecchi',
            'Shoujo', 'Horror', 'Game', 'Harem', 'Hentai']


genres_2 = ['Supernatural', 'Vampire', 'Historical', 'Super Power', 'Parody',
            'Samurai', 'Seinen', 'Police', 'Josei', 'Space', 'Kids',
            'Shoujo Ai', 'Shounen Ai', 'Cars', 'Thriller', 'Dementia',  'Yaoi',
            'Yuri', 'Martial Arts', 'Demons', 'Mecha']


class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id='your guild id here'))
            self.synced = True
        print(f'Logged on as {self.user}!')


client = MyClient()
tree = app_commands.CommandTree(client)


@tree.command(
    name='sauce',
    description='searching',
    guild=discord.Object(id='your guild id here'))
@app_commands.choices(
    genre=[app_commands.Choice(name=genre, value=genre) for genre in genres_1])
async def sauce(interaction: discord.Interaction, genre: str):
    with open(f'./datasets/{genre}.csv', 'r', encoding='utf8') as f:
        r = list(csv.reader(f))
        uid = randint(1, len(r))
        anime = r[uid]
        embed = discord.Embed(
            title=fill(f'{anime[1]} ({anime[9]}★)', 30),
            url=anime[11],
            description=fill(
                anime[3][2:-2].replace('\'', '').replace(', ', ' | '), 30),
            color=discord.Color.random()
        )
        embed.set_image(url=anime[10])
        await interaction.response.send_message(embed=embed)


@tree.command(
    name='sauce2',
    description='searching',
    guild=discord.Object(id='your guild id here'))
@app_commands.choices(
    genre=[app_commands.Choice(name=genre, value=genre) for genre in genres_2])
async def sauce2(interaction: discord.Interaction, genre: str):
    with open(f'./datasets/{genre}.csv', 'r', encoding='utf8') as f:
        r = list(csv.reader(f))
        uid = randint(1, len(r))
        anime = r[uid]
        embed = discord.Embed(
            title=fill(f'{anime[1]} ({anime[9]}★)', 30),
            url=anime[11],
            description=fill(
                anime[3][2:-2].replace('\'', '').replace(', ', ' | '), 30),
            color=discord.Color.random()
        )
        embed.set_image(url=anime[10])
        await interaction.response.send_message(embed=embed)

client.run(
    'your token here')
