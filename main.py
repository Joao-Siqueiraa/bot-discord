import discord
from discord.ext import commands, tasks
from datetime import time
from config import TOKEN,GIFBV



intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso")

#EVENTO DE BOAS VINDAS ----{
@bot.event
async def on_member_join(member:discord.Member):
    cbv = bot.get_channel(1350118330190659765)
    await cbv.send(f"{member.mention}")
    embed = discord.Embed()
    embed.title=("Boas Vindas ao Sevidor!")
    embed.description=(f"Bem-vindo(a) ao {member.guild.name}, {member.mention}!")
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_image(url=GIFBV)
    embed.set_footer(text=f"Você é o(a) membro(a) número {member.guild.member_count}!")
    
    await cbv.send(embed=embed)

#}-----


bot.run(TOKEN)
