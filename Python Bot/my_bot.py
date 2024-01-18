import asyncio
import discord
import os
from discord.ext import commands
from discord import app_commands

print("---Speicherort vorher", os.getcwd())
os.chdir(os.getcwd() + '\Python Bot')
print("---Speicherort nachher", os.getcwd())

with open('token.txt') as file:
    token = file.readlines()

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now purring!')
    status = discord.CustomActivity("g!help or /help")
    await bot.change_presence(status=discord.Status.online, activity=status)
    print(f"Status set to: {status}!")

    try:
        synced = await bot.tree.sync()
        print (f"Synced {len (synced)} command(s)")
    except Exception as e:
        print(e)

helloGIF = 'https://tenor.com/view/hi-hello-gif-1314135106863776295'
chipiGIF = 'https://tenor.com/view/chipi-chipi-chapa-chapa-cat-rainbow-cat-mizahcimtr1-gif-12949221109051297325'
ohGroguGIF = 'https://tenor.com/view/yoda-meme-yt-starwars-youtube-yoda-gif-21437903'
dancingDraginGIF = 'https://tenor.com/view/toothless-dragon-dance-boogie-happy-gif-5558141494209424671'
byeGroguGIF = 'https://tenor.com/view/baby-yoda-this-is-the-way-grogu-star-wars-yoda-gif-23259617'
hugGroguGIF = 'https://tenor.com/view/baby-yoda-hug-me-save-me-hugs-mandalorian-gif-8070753893878057805'
loveGroguGIF = 'https://tenor.com/view/star-wars-baby-yoda-cute-the-mandalorian-love-you-to-the-galaxy-and-back-gif-15834182'
sleepGroguGIF = 'https://tenor.com/view/the-mandalorian-grogu-sleeping-baby-yoda-grogu-sleeping-gif-19354118'
mainColour = 0xa2c188


@bot.tree.command (name="help")
async def hello(interaction: discord.Interaction):
    command1 = "- `Hello [bot]` / `Hallo` - greet the bot"
    command2 = "- reacting to following words: \n>>> `dance cat` / `chipi` / `chippi` / `lol` / `dance` / `hug` / `love` / `baby yoda` / \n`baby-yoda` / `bye` / `tschüss` / `tschuss` / `tschau`"
    commandSlash = "- `hello` / `slash` / `say [msg you wana tell]` / `suggest [suggestion]`"
    embedHelp=discord.Embed(title="Current Commands", description=f"{command1} \n{command2}", color=mainColour)
    embedHelp.add_field(name="slash commands", value=commandSlash, inline=True)
    await interaction.response.send_message(embed=embedHelp, ephemeral=True) #privat Msg in channel

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    print(f'{message.author}: {message.content} ---- {message.channel}')

    messageLow = message.content.lower()
    messageLowStripped = messageLow.replace(" ", "")

    if "g!help" in messageLow:
        command1 = "- `Hello [bot]` / `Hallo` - greet the bot"
        command2 = "- reacting to following words: \n>>> `dance cat` / `chipi` / `chippi` / `lol` / `dance` / `hug` / `love` / `baby yoda` / \n`baby-yoda` / `bye` / `tschüss` / `tschuss` / `tschau`"
        commandSlash = "- `hello` / `slash` / `say [msg you wana tell]`"
        embedHelp=discord.Embed(title="Current Commands", description=f"{command1} \n{command2}", color=mainColour)
        embedHelp.add_field(name="slash commands", value=commandSlash, inline=True)
        await message.channel.send(embed=embedHelp); return
    
    if "hello" in messageLow or "hallo" in messageLow:
        if messageLowStripped.startswith('hellobot'):
            await message.channel.send('Hello, human!')
            await message.channel.send(helloGIF)
            return
        else:
            await message.channel.send(helloGIF); return
    if "dancecat" in messageLowStripped or "chippi" in messageLow or "chipi" in messageLow:
        await message.channel.send(chipiGIF)
        return
    if "lol" in messageLow:
        await message.channel.send(ohGroguGIF)
        return
    if "dance" in messageLow:
        await message.channel.send(dancingDraginGIF)
        return
    if "hug" in messageLow:
        await message.channel.send(hugGroguGIF)
        return
    if "love" in messageLow:
        await message.channel.send(loveGroguGIF)
        return
    if "babyyoda" in messageLowStripped or "baby-yoda" in messageLowStripped:
        await message.channel.send("Grogu my name is!"); return
    if "bye" in messageLow or "tschüss" in messageLow or "tschuss" in messageLow or "tschau" in messageLow:
        await message.channel.send(byeGroguGIF); return

@bot.tree.command (name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.display_name}! Grogu I am!", ephemeral=True) #privat Msg in channel
    # await bot.wait_until_ready() 
    # await interaction.response.send_message(helloGIF, ephemeral=True)

@bot.tree.command (name="slash")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.display_name}! You discovered a slash command!", ephemeral=False) #public Msg channel 

@bot.tree.command (name="say")
@app_commands.describe (thing_to_say = "What should I say for you?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message (f" {interaction.user.name}: {thing_to_say}")

@bot.tree.command (name="suggest")
@app_commands.describe (suggestion = "What is your suggestion?")
async def suggestion(interaction: discord.Interaction, suggestion: str):
    print(f'User: {interaction.user.name}, Suggestion: {suggestion}')
    await interaction.response.send_message (f'Add suggestion: {suggestion}', ephemeral=True)
    await interaction.channel.send (f'suggestion: {suggestion}')

bot.run(token[0])