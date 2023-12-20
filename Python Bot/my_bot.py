import discord
import os

bot = discord.Client(intents=discord.Intents.default())
os.chdir('V:\Download\programmieren1_Bot_py\code py bot\SemOnePhyton\Python Bot')

with open('token.txt') as file:
    token = file.readline()

intentsDC = discord.Intents.default()
intentsDC.members = True

bot = discord.Client(intents=intentsDC)

bot.run(token)
