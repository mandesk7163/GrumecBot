import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configura os intents
intents = discord.Intents.default()
intents.message_content = True

# Cria o bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento quando o bot está pronto
@bot.event
async def on_ready():
    print(f"Bot está online como {bot.user}!")

# Comando simples
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Inicia o bot
bot.run(TOKEN)
