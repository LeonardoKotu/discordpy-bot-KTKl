# Информационный бот.
# 2.0 - правила, информация и т.п.

import disnake, os
from disnake.ext import commands


intents = disnake.Intents().all() # выдаем все возможности

# создание ботаv
bot = commands.InteractionBot(intents=intents)

# загрузка Когов
bot.load_extension("cogs.rules")
bot.load_extension("cogs.verify")

@bot.event
async def on_ready():
    print(f"{bot.user} is connected!")

bot.run(os.environ["DISCORD_TOKEN"])
