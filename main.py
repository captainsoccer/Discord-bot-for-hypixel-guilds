import discord
import hypixel
import requests
import asyncio
import json
import os
from discord.ext import commands
from discord.utils import get

Hypixel_Token = os.environ['HYPIXEL_TOKEN']

Discord_Token = os.environ['DISCORD_TOKEN']


API_KEYS = ['Hypixel_Token']
hypixel.setKeys(API_KEYS)
api_key = "Hypixel_Token"

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ign(ctx, args):


    user = ctx.author

    role1 = discord.utils.get(user.guild.roles, name='Guild member Role')
    role2 = discord.utils.get(user.guild.roles, name='Defualt role')

    Id = args

    username = Id

    resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    uuid = resp.json()["id"]

    Player = hypixel.Player(uuid) # This creates a Player-object and puts it to a variable called "Player".




    PlayerName = Player.getName() # This gets the player's name and puts it in a variable called "PlayerName". :3
    print("Player is called ", end='')
    print(PlayerName)

    Guild_Name = Player.getGuildID()
    print(" Player is in ", end='')
    print(Guild_Name)

    data = requests.get(f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}").json()

    Bedwars_Level = data['player']['achievements']['bedwars_level']

    Text = "\u2605{} {}".format(Bedwars_Level, args)
    await user.edit(nick=Text)


    if Guild_Name ==  "Your GUild-Id":


        await user.add_roles(role1)
        await user.remove_roles(role2)

    await ctx.message.delete()


client.run(Discord_Token)
