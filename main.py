#!/usr/bin/env python3

# a lot of this code was stolen from AVCADO/KrakenBot. infact, this was originally made as a bot that was kraken but without everything but the rolldice function
# avcado please dont yell at me
# thanks

import discord
import random
from discord.ext import commands

with open("tokenfile","r") as tokenfile:
    token = tokenfile.read()

client = commands.Bot(command_prefix="d!")
client.remove_command("help")

@client.event
async def on_ready(): # i stole the idea for printing the guilds and the invite link from kraken. i (vresod) wrote that code so it should be fine
    print("bot is ready")
    print(f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=0&scope=bot")
    for guild in client.guilds:
        print(f"In guild: {guild.name}") 

@client.event
async def on_guild_join(guild):
    print(f"Joined guild: {guild.name}")

@client.command() # i also took this from kraken
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
@client.command()
async def help(ctx):
    await ctx.send("use d!roll {number of dice} {number of sides} to roll the bones")

client.run(token)
