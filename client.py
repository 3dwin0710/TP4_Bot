import discord
from discord import Client
from setuptools import Command



default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)


#client = discord.Client()

@client.event
async def on_ready():
    print("Le bot est prêt")

@client.event
async def on_message(message):
    if message.content == "Tennis":
        await message.channel.send("de Table")

@client.event
async def on_member_join(member):
    general_channel:discord.TextChannel= client.get_channel(959348789762740233)
    await general_channel.send(content=f"欢迎{member.display_name}在我的Discord Serveur!")
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")


@client.event
async def on_member_remove(member):
    general_channel:discord.TextChannel= client.get_channel(959348789762740233)
    await general_channel.send(content=f"再见👋{member.display_name} !")
    print(f"L'utilisateur {member.display_name} a quitte le serveur !")
 
@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number+1).flatten()
        
        for each_message in messages:
            await each_message.delete()
       
@client.event
async def kick(message, user : discord.User, *reason):
   if message.content.startswith("!kick"): 
        reason = " ".join(reason)
        await message.guild.kick(user,reason = reason)
        await message.send(f"{user} a été exclu")


# Je le met en commentaire pour eviter le partage du token.
#client.run("OTU5MTk2MTI4MDAyMzMwNzE1.YkYXAQ.iD8zIV58Dn7uqr_aYLy09ccUbKY")


 
 
