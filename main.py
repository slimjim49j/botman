import discord
from discord.ext import commands
import random

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./token.env')


client = commands.Bot(command_prefix='moyai ')  # creates instance of a bot with prefix


@client.event  # function declaration- denotes that this will be an event
async def on_ready():  # when bot is ready
    print('MoyaiBotMan is ready')


# @client.event
# async def on_connect(message):
#    await message.channel.send('MoyaiBotMan online')


#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith('moyai!'):
#        await message.channel.send(':moyai:')


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

client.run(os.getenv("TOKEN"))

