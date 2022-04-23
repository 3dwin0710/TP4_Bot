#from click import command
import discord
import logging
from discord.ext import commands


class Logginclass(commands.Cog):
  
  def __init__(self):
      super().__init__()
      self.log();
  
  def log():
    #logging.getLogger("discord").setLevel(logging.WARNING)
    logging.basicConfig(filename="discord.log", level=logging.INFO,format="%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    #ogging.getLogger('discord').setLevel(logging.DEBUG)
    #handler = logging.FileHandler(filename='test.log', encoding='utf-8', mode='w',datefmt='%Y-%m-%d %H:%M:%S')
    #handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    #logger.addHandler(handler)
    
  def debugLog(msg):
    logging.debug(msg)
  
  def warningLog(msg):
    logging.warning(msg)
  
  def infoLog(msg):
    logging.info(msg)
  
  


    
    
  