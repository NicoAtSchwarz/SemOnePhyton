import discord
import os
from discord.ext import commands

print("Speicherort", os.chdir)
os.chdir(os.getcwd() + '\Python Bot')
print("Speicherort", os.chdir)

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

with open('token.txt') as file:
    token = file.readlines()

helloGIF = 'https://tenor.com/view/hi-hello-gif-1314135106863776295'

@bot.event
async def on_startup():
    print('The bot has started!')

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    print(f'Received message from {message.author}: {message.content} ---- {message.channel}')

    if message.content.lower().startswith('hello bot'):
        print("Hello bot")
        await message.channel.send('Hello, human!')

    if "hello" or "hallo" in message.content.lower().lstrip():
        print("Hallo oder Hello!")
        await message.channel.send(helloGIF)

bot.run(token)