from keep_alive import keep_alive
keep_alive()

import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

load_dotenv()
token = os.getenv("TOKEN")
bot.run(token)
