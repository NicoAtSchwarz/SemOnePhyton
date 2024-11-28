import asyncio
import discord #Python 3.11.3 needed
import os
from discord.ext import commands
from discord import app_commands

print("---Speicherort vorher", os.getcwd())
os.chdir(os.getcwd() + '\Python Bot')
print("---Speicherort nachher", os.getcwd())

with open('token.txt') as file:
    token = file.readlines()

with open('log.txt') as file:
    list = file.readlines()
    logGuild = int(list[0])
    logChannel = int(list[1]) #general Channel
    logChannelDM = int(list[2]) #direktMsg Channel
    logChannelMsg = int(list[3]) #Msg Channel
    logChannelMember = int(list[4]) #Member Channel
    creatorID = int(list[5]) #Creator ID
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='g!', intents=intents)

async def print_log_info():
    guild = await bot.fetch_guild(logGuild)
    user = bot.get_user(creatorID)

    print("logGuild: ", logGuild, guild.name)
    print("logChannel: ", logChannel, bot.get_channel(logChannel).name)
    print("logChannelDM: ", logChannelDM, bot.get_channel(logChannelDM).name)
    print("logChanneMsg: ", logChannelMsg, bot.get_channel(logChannelMsg).name)
    print("logChannelMember: ", logChannelMember, bot.get_channel(logChannelMember).name)
    print("creatorID: ", creatorID, user.name)

@bot.event
async def on_ready():
    await print_log_info()
    print(f'{bot.user} is now online!')
    #status = discord.CustomActivity("g!help or /help")
    status = discord.CustomActivity("teste meine slash commands")
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

doneGIF = "https://cdn.discordapp.com/attachments/1029502275208630414/1032604402596466748/haken.gif?ex=65bb754a&is=65a9004a&hm=9ff350aef78e2b974dea2ff197082d116e21f0dd076b8f0b9d0ccb045721547a&"
mainColour = 0xa2c188

greetCommands = "- `Hello [bot]` / `Hallo [bot]` - greet the bot"
reactingWords = ["dance cat", "chipi", "chippi", "baby yoda", "baby-yoda"]
reactingWords.sort
wordCommands = "- reacting to following words: \n>>> "
for x in reactingWords:
    wordCommands += f" `{x}` /"
#print("vorher:", wordCommands)
wordCommands = wordCommands[:-2]
#print("nachher:", wordCommands)

slashWords = ["bye", "chipi", "dance", "dm-hello [member]", "hello", "hug", "id [member]", "lol", "love", "say [msg you wana tell]", "slash", "suggest [suggestion]", "whisper [member] [message]"]
slashWords.sort
slashCommands = "- `help`:"
for x in slashWords:
    slashCommands += f" `{x}` /"
#print("vorher:", slashCommands)
slashCommands = slashCommands[:-2]
#print("nachher:", slashCommands)

@bot.tree.command (name="help", description="Help with everything")
async def help(interaction: discord.Interaction):
    embedHelp=discord.Embed(title="Current Commands", description=f"{greetCommands} \n{wordCommands}", color=mainColour)
    embedHelp.add_field(name="slash commands", value=slashCommands, inline=True)
    await interaction.response.send_message(embed=embedHelp, ephemeral=True) #privat Msg in channel


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    #(f'{message.author}: {message.content} ---- #{message.channel} -+- {message.guild}')

    messageLow = message.content.lower()
    messageLowStripped = messageLow.replace(" ", "")

    if "g!help" in messageLow:
        embedHelp=discord.Embed(title="Current Commands", description=f"{greetCommands} \n{wordCommands}", color=mainColour)
        embedHelp.add_field(name="slash commands", value=slashCommands, inline=True)
        await message.channel.send(embed=embedHelp); return
    
    if "hello" in messageLow or "hallo" in messageLow:
        if messageLowStripped.startswith('hellobot'):
            await message.channel.send('Hello, human!')
            await message.channel.send(helloGIF)
            return
        elif messageLowStripped.startswith('hallobot'):
            await message.channel.send('Hallo, Mensch!')
            await message.channel.send(helloGIF)
        else:
            await message.channel.send(helloGIF); return
    if "dancecat" in messageLowStripped or "chippi" in messageLow or "chipi" in messageLow:
        await message.channel.send(chipiGIF)
        return
    if "babyyoda" in messageLowStripped or "baby-yoda" in messageLowStripped:
        await message.channel.send("Grogu my name is!"); return

@bot.tree.command (name="bye", description="Bye👋")
async def bye(interaction: discord.Interaction):
    await interaction.response.send_message(byeGroguGIF, ephemeral=False) #public Msg channel

@bot.tree.command (name="chipi", description="Chipi chipi, chapa chapa...")
async def chipi(interaction: discord.Interaction):
    await interaction.response.send_message(chipiGIF, ephemeral=False) #public Msg channel 

@bot.tree.command (name="dance", description="Let's dance!")
async def dance(interaction: discord.Interaction):
    await interaction.response.send_message(dancingDraginGIF, ephemeral=False) #public Msg channel 

@bot.tree.command (name="hello", description="Say Hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.display_name}! Grogu I am!", ephemeral=False) #public Msg channel
    await interaction.channel.send(helloGIF)

@bot.tree.command (name="hug", description="Send a hug!")
async def hug(interaction: discord.Interaction):
    await interaction.response.send_message(hugGroguGIF, ephemeral=False) #public Msg channel 

@bot.tree.command (name="lol", description="Let's dance!")
async def lol(interaction: discord.Interaction):
    await interaction.response.send_message(ohGroguGIF, ephemeral=False) #public Msg channel 

@bot.tree.command (name="love", description="Send love!")
async def love(interaction: discord.Interaction):
    await interaction.response.send_message(loveGroguGIF, ephemeral=False) #public Msg channel 

@bot.tree.command (name="say", description="Say me, what I should tell the others")
@app_commands.describe (thing_to_say = "What should I say for you?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    print(f'User: {interaction.user.name}, Say: {thing_to_say}, Guild: {interaction.guild}, Channel: {interaction.channel}')
    await interaction.response.send_message (f" {interaction.user.name}: {thing_to_say}")

@bot.tree.command (name="slash", description="Explore slash commands")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.display_name}! You discovered a slash command!", ephemeral=False) #public Msg channel 

@bot.tree.command (name="suggest", description="Make a suggestion")
@app_commands.describe (suggestion = "What is your suggestion?")
async def suggestion(interaction: discord.Interaction, suggestion: str):
    print(f'User: {interaction.user.name}, Suggestion: {suggestion}, Guild: {interaction.guild}, Channel: {interaction.channel}')
    await interaction.response.send_message (f'Add suggestion: {suggestion}', ephemeral=True)
    await interaction.channel.send (f'suggestion: {suggestion}')

@bot.tree.command (name="id", description="Get the ID of a member")
async def userid(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"ID of {member.global_name}: {member.id}", ephemeral=True)

@bot.tree.command(name="dm-hello", description="Send a DM")
async def dm(interaction: discord.Interaction, member: discord.Member):
    messageSend = f"{interaction.user.global_name} sends you a: `Hello`"
    await interaction.response.send_message(f"Message to {member.global_name}: {messageSend}", ephemeral=True)
    await member.send(f"{messageSend}")
    await logMessage("DM", f"{interaction.user.global_name} sends a `Hello` to {member.global_name}.")

@bot.tree.command(name="whisper", description="Send a DM to somebody")
async def dm(interaction: discord.Interaction, member: discord.Member, whisper :str):
    messageSend = f"{interaction.user.global_name} whispers you: {whisper}"
    await interaction.response.send_message(f"Message to {member.global_name}: {messageSend}", ephemeral=True)
    await member.send(f"{messageSend}")
    await logMessage("", f"{interaction.user.global_name} whisper to {member.global_name}: {whisper}")

@bot.tree.command(name="dm-message", description="Send a Message to someone")
async def dm(interaction: discord.Interaction, member: discord.User, message: str):
    messageSend = f"{interaction.user.global_name} to you: {message}"
    await interaction.response.send_message(messageSend, ephemeral=True)
    await member.send(messageSend)
    await logMessage("DM", messageSend)

@bot.tree.command(name="clear",description="Delete Messages automatically from the current channel")
async def clear(interaction: discord.Interaction, number:int, member:discord.Member = None):
    if number > 50:
        number = 50
    def check_(m):
        return m.author == member
    if not member:
        await interaction.channel.purge(limit=number)
    else:
        await interaction.channel.purge(limit=number,check=check_)
    await interaction.response.send_message(f"Deleted: {number}, from this channel.", ephemeral=True)
    await logMessage("MSG", f"Deleted: {number} Messages, \nfrom channel \{interaction.channel} \ndue to \n{interaction.user.global_name}.")

async def logMessage(guilID:int, channel:str, msg: str):
    if guilID == logGuild:
        return
    target_guild = bot.get_guild(logGuild)
    if target_guild:
        if channel == "DM":
            target_channel = target_guild.get_channel(logChannelDM)
        elif channel == "MSG":
            target_channel = target_guild.get_channel(logChannelMsg)
        elif channel == "USER":
            target_channel = target_guild.get_channel(logChannelMember)
        else:
            target_channel = target_guild.get_channel(logChannel)

        if target_channel:
            await target_channel.send(f"{msg}")
        else:
            print(f"Target channel with ID {logChannel} not found.")
    else:
        print(f"Target guild with ID {logGuild} not found.")
    
@bot.event
async def on_message_delete(message: discord.Message):
    await logMessage("MSG", f"Deleted: {message.content}, from channel {message.channel} due to {message.author.global_name} on {message.guild.name}.")
@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    await logMessage(before.guild.id, "MSG", f"Edited: \n{before.content}, \n\nto: \n{after.content}, \nfrom channel {before.channel} due to {before.author.global_name} on {after.guild.name}.")
@bot.event
async def on_member_join(member: discord.Member):
    await logMessage(0, "USER", f"{member.global_name} joined {member.guild.name}.")
@bot.event
async def on_member_remove(member: discord.Member):
    await logMessage(0, "USER", f"{member.global_name} left {member.guild.name}.")
@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    if before.nick != after.nick:
        await logMessage(0, "USER", f"{before.name} changed their nickname from {before.nick} to {after.nick} at {after.guild.name}.")

bot.run(token[0])