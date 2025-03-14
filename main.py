import discord
from discord.ext import commands, tasks
from datetime import time
from config import TOKEN



intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso")






bot.run(TOKEN)
