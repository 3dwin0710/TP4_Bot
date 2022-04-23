import os
import discord
from dotenv import load_dotenv

from Logger.Logging import Logginclass
from discord.ext import commands
import logging #imports Discord.py logging module


load_dotenv(dotenv_path="config")
Logginclass.log()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents) # test pour remove un user mais cela ne fonctionne pas
import discord

class Docbot(discord.ext.commands.Cog, name='Docbot module'):
    def __init__(self, bot):
        self.bot = bot
        
    # Test pour appeler à l'aide  
    @commands.command(name="Helpo")
    async def test(self, ctx):
        await ctx.send(f'Help {ctx.author.name}')

      
    # Supprimer les messager avec un range
    @commands.command(name="del")
    async def on_message(self,ctx,number_of_message:int):
            messages = await ctx.channel.history(limit=number_of_message+1).flatten()
            
            for each_message in messages:
                await each_message.delete()
    # Pour afficher un message de bienvenue au nouveau arrivant:   
    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'欢迎{member.mention}在我的Discord Serveur!')
    
    
    # Test pour faire l'operation en envoyant un message, le bot m'envoie en retour un autre message.
    @commands.command(name="Tennis")
    async def Miror(self, ctx):
        await ctx.send("De Table")
        message = "Tennis De Table!Un sport a ne pas sous-estimer"
        logging.getLogger("Logger").info(message)
        
	   # print(f"{ctx.message.author.name} says " + str(ctx.message.content))
		#Logginclass.infoLog(msg)
        
    # Fonction Help pour afficher toutes les fonctions sur mon Tp
    @commands.command(name="Help")
    async def help(self,ctx):
        em = discord.Embed(title = "Help", description ="Use >help< Liste de commande")
        em.add_field(name="Moderation", value="Kick <member> [reason]")
        em.add_field(name="Moderation",value="Ban <member> [reason]")
        em.add_field(name="Moderation",value="Delete <message> [reason] ")
        em.add_field(name="Rappel",value="Help <general> [reason]")
        em.add_field(name ="Achtung", value="Respect")
        message = "Utilisation de la fonction Help pour connaitre ce que mon serveur a comme fonction"
        logging.getLogger("Logger").info(message)
        Logginclass.warningLog(message)
        await ctx.send(embed = em)
    
    #Cette fonction ne fonctionne pas trop..  
    @discord.ext.commands.Cog.listener()  
    async def on_member_remove(self,member):
        general_channel:discord.TextChannel= bot.get_channel(959348789762740233)
        await general_channel.send(content=f"再见👋{member.display_name} !")
        print(f"L'utilisateur {member.display_name} a quitté le serveur !")
    #logging.getLogger("Logger").info(f" L'utilisateur{member.display_name} a quitté le serveur !")

    
    
    #logging.getLogger("Logger").info(f" L'utilisateur{member.display_name} a quitté le serveur !")



#bot.run(os.getenv("Token"))