import discord

bot = discord.Client(intents=discord.Intents.default())

with open("token.txt", "r") as file:
    token = file.readline().strip()

dcIntents = discord.Intents.default()
dcIntents.members = True

bot = discord.Client(intents=dcIntents)

bot.run(token)