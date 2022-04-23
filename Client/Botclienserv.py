from discord.ext import commands
import discord 
import logging
from Logger.Logging import Logginclass

Logginclass.log()
class CustomBotClient(commands.Bot):
    async def on_ready(self):
        print(f'{self.user.name} est prêt!') 
        msg = f"{self.user.display_name} est connecté au serveur."
        logging.getLogger("Logger").info(f"{self.user.display_name} est connecté au serveur.")
        Logginclass.warningLog(msg)
        Logginclass.infoLog(msg)

    
        
#token = "OTU5MTk2MTI4MDAyMzMwNzE1.YkYXAQ.iD8zIV58Dn7uqr_aYLy09ccUbKY"



