import nextcord
from nextcord.ext import commands
import os
import logging
import random

TOKEN = os.getenv("MOGUBOT_TOKEN")

bot = commands.Bot(command_prefix="t?", description="Tommybot is a custom bot made for Tommylore and Sas, made by >>#0001.", owner_ids={956698441361260567,743340045628342324,901978388829450291})

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message: nextcord.Message):
    if "bladee" in message.lower():
        await message.channel.send("kys")

@bot.command()
async def poll(ctx):
    await ctx.message.add_reaction("<:tommythumbsup:946649096645664768>")
    await ctx.message.add_reaction("<:tommythumbsdown:947042965484896287>")

@bot.command()
async def activity(ctx, *args):
    if await bot.is_owner(ctx.author):
    
        args = list(args)
        try:
            status_type = args[0]
            new_status = ' '.join(args[1:])
        except:
            await ctx.send(embed=nextcord.Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `t!activity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
        else:
            if len(args) > 1:
                if status_type == "playing":
                    await bot.change_presence(activity=nextcord.Game(name=new_status))
                    await ctx.send(embed=nextcord.Embed(title="Success",description=f"Activity successfully changed to \"Playing {new_status}\".", color=0x00ff00))
                elif status_type == "streaming":
                    await bot.change_presence(activity=nextcord.Streaming(name=new_status, url="https://google.com"))
                    await ctx.send(embed=nextcord.Embed(title="Success", description=f"Activity successfully changed to \"Streaming {new_status}\".", color=0x00ff00))
                elif status_type == "listening":
                    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=new_status))
                    await ctx.send(embed=nextcord.Embed(title="Success", description=f"Activity successfully changed to \"Listening to {new_status}\".", color=0x00ff00))
                elif status_type == "watching":
                    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=new_status))
                    await ctx.send(embed=nextcord.Embed(title="Success", description=f"Activity successfully changed to \"Watching {new_status}\".", color=0x00ff00))
                else:
                    await ctx.send(embed=nextcord.Embed(title="Error", description=f"Improper arguments\n\nProper command format: `t!activity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
            else:
                await ctx.send(embed=nextcord.Embed(title="Error", description=f"Not enough arguments\n\nProper command format: `t!activity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))

    else:
        await ctx.send("lol no")
    
# add new commands before this line
bot.run(TOKEN)