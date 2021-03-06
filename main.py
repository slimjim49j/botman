from Controller.Fight_Controller import Fight_Controller
import discord
from discord.ext import commands
import random
import math

import os

from Model.Player import Player

from dotenv import load_dotenv

load_dotenv(dotenv_path='./token.env')


# creates instance of a bot with prefix
client = commands.Bot(command_prefix='moyai ')


@client.event  # function declaration- denotes that this will be an event
async def on_ready():  # when bot is ready
    print('MoyaiBotMan is ready')

# @client.event
# async def on_connect(message):
#    await message.channel.send('MoyaiBotMan online')


# @client.event
# async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith('moyai!'):
#        await message.channel.send(':moyai:')


@client.command()
async def hunt(ctx):

    # get user ID
    newUserID = ctx.author.id
    # get player object associated with ID
    player_object = Player.get_player(newUserID)

    Fight_Controller.create_hunt(newUserID)

    # create enemy
    new_enemy = Enemy()
    # create fight
    # announce winner
    # distribute spoils if any

    pass


# Engage combat between player and another player
@client.command()
async def fight(ctx):
    pass


@client.command()
async def ping(ctx):  # when command "ping" is typed
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

emojis = []

# not really sure what that for loop does, more info
# https://towardsdatascience.com/filtering-lists-in-python-a3387c7b6b5e


async def get_moyai_emojis():
    guild = await client.fetch_guild(801989557309538325)
    guild_emojis = guild.emojis
    return [emoji for emoji in guild_emojis if "moy" in emoji.name]

# using global vars:
# https://www.w3schools.com/python/python_variables_global.asp


@client.command(aliases=['please', 'want'])
async def give(ctx, *, statement):  # * allows you to take multiple arguments
    global emojis
    if not emojis:
        emojis = await get_moyai_emojis()

    await ctx.send(f'You just said: {statement}\n And for that I will give you: {random.choice(emojis)}')


@client.command(aliases=['make-it-rain'])
async def rain(ctx):
    global emojis
    if not emojis:
        emojis = await get_moyai_emojis()

    await ctx.send("Make it raaaaiin!!!\n")
    for i in range(10):
        message = ""
        for j in range(10):
            message += f'{random.choice(emojis)}' + \
                (math.floor(random.random() * 100) * " ")
        await ctx.send(message)

client.run(os.getenv("TOKEN"))
