import os
import discord
from dotenv import load_dotenv
import logging
from Logging import Logginclass
from discord.ext import commands


load_dotenv(dotenv_path="config")



class DocBot(commands.Bot):
    def __init__(self):
       super().__init__(command_prefix="!")
        
    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")
        logging.getLogger("Logger").info(f"{self.user.display_name} est connecté au serveur.")
        msg = f"{self.user.display_name} est connecté au serveur."
        Logginclass.warningLog(msg)
        Logginclass.infoLog(msg)

    
    async def on_message(self,name ='Tennis'):
        if name.content == "Tennis":
             await name.channel.send("de Table")
             logging.getLogger("Logger").info(f"{self.user.display_name} send Tennis")
             logging.getLogger("Logger").info(f"{self.user.display_name} send de Table")
      
    @discord.ext.commands.command(name="del") 
    async def on_message(self,ctx,number_of_message:int):
            messages = await ctx.channel.history(limit=number_of_message+1).flatten()
            
            for each_message in messages:
                await each_message.delete()          
    #bot.remove_command("help")  
    #@bot.group(invoke_without_command=True)  
'''
    async def help(self,ctx):
        em = discord.Embed(title = "Help", description ="Use >help< Liste de commande")
        em.add_field(name="Moderation", value="Kick <member> [reason]")
        em.add_field(name="Moderation",value="Ban <member> [reason]")
        em.add_field(name="Moderation",value="Unban <member> [reason] ")
        em.add_field(name="Moderation",value="Unban <member> [reason]")
        em.add_field(name ="Achtung", value="Respect")
     
    
        await ctx.send(embed = em)
    
    async def delete(self,ctx,number_of_message:int):
        
        messages = await ctx.channel.history(limit=number_of_message+1).flatten()
        for each_message in messages:
          await each_message.delete()
    '''
 
Logginclass.log();
    
doc_bot = DocBot()
doc_bot.run(os.getenv("Token"))
    

    