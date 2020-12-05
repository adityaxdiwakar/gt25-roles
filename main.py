from bs4 import BeautifulSoup
from dotenv import load_dotenv
import datetime
import requests
import os

load_dotenv() #grab env variables from config

from utils import reactions

import copy
import discord
import time
import asyncio
import ast

intents = discord.Intents.default()
intents.members = True

class Stella(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_raw_reaction_add(self, payload):
        await reactions.handler(self, payload, "add")

    async def on_raw_reaction_remove(self, payload):
        await reactions.handler(self, payload, "remove")



ctx = Stella()
ctx.run(os.getenv("BOT_TOKEN"))