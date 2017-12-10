# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from os import listdir, getcwd
from os.path import isfile, join
import random

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Habchy#1665", command_prefix="-", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Support Discord Server: https://discord.gg/FNNNgqb')
    print('Github Link: https://github.com/Habchy/BasicBot')
    print('--------')
    print('Created by Habchy#1665')

async def variables():
    await client.wait_until_ready()
    n = 0

@client.command()
async def 츄르(*args):
    await client.say("배불러냥 그만하라냥")

@client.command(pass_context = True)
async def 쓰담(ctx):
    await client.say("그릉그릉 ("+str(variables().n)+"번 쓰담)")

@client.command(pass_context = True)
async def 지냥짤(ctx):
    channel = ctx.message.channel

    path = "/Pics/"
    files = [f for f in listdir(getcwd()+path) if isfile(join(getcwd()+path, f))]

    name = random.choice(files)
    with open("Pics/"+name, 'rb') as f:
        await client.send_file(channel, f)

client.loop.create_task(variables())
client.run('Mzg2OTAwMjExMzkxMjY2ODE2.DQWpAA.tXe5ththdd6OaGwq2ZpnUEjnP6k')