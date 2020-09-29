#!/usr/bin/env python3
import discord
import random
from discord.ext import commands

with open("tokenfile","r") as tokenfile:
    token = tokenfile.read()

client = commands.Bot(command_prefix="d!")
client.remove_command("help")

@client.event
async def on_ready():
    print("bot is ready")
    print(f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=0&scope=bot")
    for guild in client.guilds:
        print(f"In guild: {guild.name}") 

@client.event
async def on_guild_join(guild):
    print(f"Joined guild: {guild.name}")

@client.command()
async def rollDice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

client.run(token)
