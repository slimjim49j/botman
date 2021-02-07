import discord
from discord.ext import commands
import random

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


@client.command(aliases=['please', 'want'])
async def give(ctx, *, statement):  # * allows you to take multiple arguments
    responses = ['Moyai',
                 'Epic moyai',
                 ':moyai:']
    await ctx.send(f'You just said: {statement}\n And for that I will give you: {random.choice(responses)}')


client.run('ODA3NjYyMDYyOTc2NDk5NzYy.YB7P6Q.oSLuicqEHbPziyzg4wANIzfKN64')
