#from distutils.command.config import config
#from typing import get_args
import discord
import os
from Client.Botclienserv import CustomBotClient
from Bot.Classlogbot import Docbot
from dotenv import load_dotenv
import argparse
from argparse import ArgumentParser
import json



def main():
  load_dotenv(dotenv_path="config")
#token = "OTU5MTk2MTI4MDAyMzMwNzE1.YkYXAQ.iD8zIV58Dn7uqr_aYLy09ccUbKY"

  intents = discord.Intents.default()
  intents.members = True

  bot = CustomBotClient(
        command_prefix='!', 
        intents=intents 
        )

  bot.add_cog(Docbot(bot))
#add_cog est une méthode de discord

#bot.run(token)
  bot.run(os.getenv("Token"))


def parse_args():
  parser = ArgumentParser()
  parser.add_argument('-c', '--config', help='Config file', required=True, dest='config')
  return parser.parse_args()



if __name__ == '__main__':
        #arg = parse_args()
        main()