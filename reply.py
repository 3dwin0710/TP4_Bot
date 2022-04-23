import logging
import os
from tokenize import Token
import discord
from discord.ext import commands
#import dotenv
from dotenv import load_dotenv
from Logger.Logging import Logginclass





load_dotenv(dotenv_path="config")
#bot = commands.Bot(command_prefix = "!",description = "Bot de Boty")
'''
@bot.event
async def on_ready():
    print("Ready !!")

@bot.command()
async def coucou(ctx):
    await context.send("Coucou !")
'''
#bot.run("OTU5MTk2MTI4MDAyMzMwNzE1.YkYXAQ.ctwRI2nud-yaQ-9-9OB7UJGW4sQ")


default_intents = discord.Intents.default()
default_intents.members = True


#Logginclass.log();
bot = commands.Bot(command_prefix="!",intents=default_intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Le bot est prêt")
    #logging.getLogger("Logger").info("Yes we dit it!")
    
'''  
@bot.event
async def on_message(name ='Tennis'):
    if name.content == "Tennis":
        await name.channel.send("de Table")
        print("Tableeee")
        #user = bot.get_user(bot.user.id)
       # logging.getLogger("Logger").info("user send Tennis")
        #logging.getLogger("Logger").info(" {bot.user.id} send de Table")
 '''   
@bot.command(name='del')
async def on_message(ctx,number_of_message:int):
    messages = await ctx.channel.history(limit=number_of_message+1).flatten()
    for each_message in messages:
            await each_message.delete()
'''
@bot.command(name="out")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked!")
'''	
@bot.event
async def on_member_join(member):
    general_channel:discord.TextChannel= bot.get_channel(959348789762740233)
    await general_channel.send(content=f"欢迎{member.display_name}在我的Discord Serveur!")
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")


@bot.command(name='kick')
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    print(reason)
    await ctx.guild.kick(user,reason = reason)
    await ctx.send(f"{user} a été exclu")
    


@bot.event
async def on_member_join(member):
    general_channel:discord.TextChannel= bot.get_channel(959348789762740233)
    await general_channel.send(content=f"欢迎{member.display_name}在我的Discord Serveur!")
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
    #logging.getLogger("Logger").info(f" L'utilisateur{member.display_name} a rejoint le serveur !")


@bot.event
async def on_member_remove(member):
    general_channel:discord.TextChannel= bot.get_channel(959348789762740233)
    await general_channel.send(content=f"再见👋{member.display_name} !")
    print(f"L'utilisateur {member.display_name} a quitté le serveur !")
    #logging.getLogger("Logger").info(f" L'utilisateur{member.display_name} a quitté le serveur !")

 
    
@bot.command(name='ban')
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} a été ban pour la raison suivante: {reason}.")
    
@bot.command(name='unban')
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split('#')
    Banusers = await ctx.guild.bans()
    for i in Banusers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} a été unban")
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description ="Use >help< Liste de commande")
    em.add_field(name="Moderation", value="Kick <member> [reason]")
    em.add_field(name="Moderation",value="Ban <member> [reason]")
    em.add_field(name="Moderation",value="Unban <member> [reason] ")
    em.add_field(name="Moderation",value="Unban <member> [reason]")
    em.add_field(name ="Achtung", value="Respect")
   
    
    await ctx.send(embed = em)
    

bot.run(os.getenv("Token"))
#bot.run("OTU5MTk2MTI4MDAyMzMwNzE1.YkYXAQ.iD8zIV58Dn7uqr_aYLy09ccUbKY")
#Fichier Test