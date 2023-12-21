import discord

bot = discord.Client()

# run client
with open('token.txt') as file:
    token = file.readlines()


dcIntents = discord.Intents.default()
dcIntents.members = True

bot = discord.Client(intents=dcIntents)

bot.run(token)