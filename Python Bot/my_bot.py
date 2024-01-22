import asyncio
import discord
import os
from discord.ext import commands

print("---Speicherort vorher", os.getcwd())
os.chdir(os.getcwd() + '\Python Bot')
print("---Speicherort nachher", os.getcwd())

with open('token.txt') as file:
    token = file.readlines()

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='g!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now purring!')

helloGIF = 'https://tenor.com/view/hi-hello-gif-1314135106863776295'
chipiGIF = 'https://tenor.com/view/chipi-chipi-chapa-chapa-cat-rainbow-cat-mizahcimtr1-gif-12949221109051297325'
ohGroguGIF = 'https://tenor.com/view/yoda-meme-yt-starwars-youtube-yoda-gif-21437903'
dancingDraginGIF = 'https://tenor.com/view/toothless-dragon-dance-boogie-happy-gif-5558141494209424671'
byeGroguGIF = 'https://tenor.com/view/baby-yoda-this-is-the-way-grogu-star-wars-yoda-gif-23259617'
hugGroguGIF = 'https://tenor.com/view/baby-yoda-hug-me-save-me-hugs-mandalorian-gif-8070753893878057805'
loveGroguGIF = 'https://tenor.com/view/star-wars-baby-yoda-cute-the-mandalorian-love-you-to-the-galaxy-and-back-gif-15834182'
sleepGroguGIF = 'https://tenor.com/view/the-mandalorian-grogu-sleeping-baby-yoda-grogu-sleeping-gif-19354118'

sendHelpMSG = "**Current Commands** \n'Hello [bot]' / 'Hallo' - greet the bot \n'dance cat' / 'chipi' / 'chippi'"

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    print(f'{message.author}: {message.content} ---- {message.channel}')

    messageLow = message.content.lower()
    messageLowStripped = messageLow.replace(" ", "")

    if "help" in messageLow:
        await message.reply(sendHelpMSG); return
    
    if "hello" in messageLow or "hallo" in messageLow:
        if messageLow.startswith('hello bot'):
            await message.channel.send('Hello, human!')
            await message.channel.send(helloGIF); return
        else:
            await message.channel.send(helloGIF); return

    if "dancecat" in messageLowStripped or "chippi" in messageLow or "chipi" in messageLow:
        await message.channel.send(chipiGIF); return
    
    if "lol" in messageLow: await message.channel.send(ohGroguGIF); return
    
    if "dance" in messageLow:
        await message.channel.send(dancingDraginGIF); return
    
    if "hug" in messageLow: await message.channel.send(hugGroguGIF); return

    if "love" in messageLow:await message.channel.send(loveGroguGIF); return
    
    if "bye" in messageLow or "tschüss" in messageLow or "tschuss" in messageLow or "tschau" in messageLow: await message.channel.send(byeGroguGIF); return
    
    bot.run(token[0])

    #main entry point
def main()-> None:
    bot.run(token[0])

if __name__ == '__main__':
    main()