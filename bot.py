import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Přihlášen jako {client.user}")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        await channel.send(f"👋 Vítej {member.mention} na serveru!")

client.run(os.getenv("TOKEN"))

