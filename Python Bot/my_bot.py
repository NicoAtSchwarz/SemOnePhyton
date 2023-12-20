import discord
import os
from discord.ext import commands

os.chdir(os.getcwd() + '\Python Bot')

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

with open('token.txt') as file:
    token = file.readline()

@bot.event
async def on_startup():
    print('The bot has started!')

@bot.event
async def on_message(message):
    if message.author == bot:
        return
    
    # Your code to process the message here
    print(f'Received message from {message.author}: {message.content} ---- {message.channel}')

bot.run(token)
