# CONFIG
# ---------
token = "TOKEN_HERE" # To find this, press CTRL + SHIFT + i in the Discord client revealing the inspect element prompt. Click the arrows, head over to Application, local storage and there you can find your user token :)
prefix = "~" # This will be used at the start of commands.
rename_to = "Innocent" # The string everyone possible will be renamed to using the 'rall' command.
# ----------

import discord
from discord.ext import commands
from discord.ext.commands import Bot

print ("Loading..")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Ready to be innocent.")

@bot.command(pass_context=True)
async def kall(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.kick(user)
                print (user.name + " has been kicked from " + ctx.message.server.name)
            except:
                pass    
        print ("Action Completed: kall")

@bot.command(pass_context=True)
async def ball(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
                print (user.name + " has been banned from " + ctx.message.server.name)
            except:
                pass 
        print ("Action Completed: ball")  

@bot.command(pass_context=True)
async def rall(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.change_nickname(user, rename_to)
                print (user.name + " has been renamed to " + rename_to + " in " + ctx.message.server.name)
            except:
                pass
        print ("Action Completed: rall")

bot.run(token, bot=False)