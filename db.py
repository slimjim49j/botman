import psycopg2 as pg2
import discord
from discord.ext import commands
import random
import math
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./token.env')

# creates instance of a bot with prefix
client = commands.Bot(command_prefix='moyai ')
guildID = 801989557309538325


@client.event  # function declaration- denotes that this will be an event
async def on_ready():  # when bot is ready
    print('MoyaiBotMan is ready')

# create connection to database
conn = pg2.connect(database=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
                   password=os.getenv("DB_PASSWORD"))

# create cursor to database
cur = conn.cursor()

emojis = []

# not really sure what that for loop does, more info
# https://towardsdatascience.com/filtering-lists-in-python-a3387c7b6b5e

# gets emoji from guild


async def get_moyai_emojis():
    guild = await client.fetch_guild(guildID)
    guild_emojis = guild.emojis
    return [emoji for emoji in guild_emojis if "moy" in emoji.name]

# setFavorite will get a random emoji, then assign the emoji to a unique user


@client.command(aliases=['insert', 'in'])
async def setFavorite(ctx):
    global emojis
    if not emojis:
        emojis = await get_moyai_emojis()

    # gets random emoji with unique user id
    newFavEmoji = random.choice(emojis).id
    newUserID = ctx.author.id
    print(type(newFavEmoji))

    # insert values of userID and emoji as a pair in to table
    # note: favMoyTable consists of two columns: bigInt userID and bigInt favMoy
    cur.execute(
        f"INSERT INTO favMoyTable (userID, favMoy) VALUES({newUserID}, {newFavEmoji});")

    # commit and close- need to move where connection closes for multiple querries
    conn.commit()
    conn.close()

    await ctx.send(f'Your newly assigned favorite moyai is now {newFavEmoji}')

# prints out emoji assigned to player


@client.command(aliases=['retrieve'])
async def getFavorite(ctx):
    cur.execute("SELECT * FROM favMoyTable")
    allPairings = cur.fetchall()
    for pair in allPairings:
        if ctx.author.id == pair[0]:
            await ctx.send(f'Your favorite moyai is {pair[1]}')


client.run(os.getenv("TOKEN"))
