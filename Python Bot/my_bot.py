import asyncio
import discord
import os
from discord.ext import commands

print("---Speicherort vorher", os.getcwd())
os.chdir(os.getcwd() + '\SemOnePhyton\Python Bot')
print("---Speicherort nachher", os.getcwd())

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

with open('token.txt') as file:
    token = file.readlines()

helloGIF = 'https://tenor.com/view/hi-hello-gif-1314135106863776295'
chipiGIF = 'https://tenor.com/view/chipi-chipi-chapa-chapa-cat-rainbow-cat-mizahcimtr1-gif-12949221109051297325'
sendHelpMSG = "**Current Commands \n'Hello [bot]' / 'Hallo' - greet the bot \n'dance cat' / 'chipi' / 'chippi'"

@bot.event
async def on_startup():
    print('The bot has started!')

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    print(f'{message.author}: {message.content} ---- {message.channel}')

    if "help" in message.content.lower():
        await message.reply(sendHelpMSG)
    
    if "hello" in message.content.lower() or "hallo" in message.content.lower():
        if message.content.lower().startswith('hello bot'):
            print("Hello bot")
            await message.channel.send('Hello, human!')
            return
        else:
            await message.channel.send(helloGIF)
            print("Hallo oder Hello!")
            return

    if "dancecat" in message.content.lower().replace(" ", "") or "chippi" in message.content.lower() or "chipi" in message.content.lower():
        await message.channel.send(chipiGIF)
        await asyncio.sleep(3)
        await message.delete()
        return

bot.run(token[0])