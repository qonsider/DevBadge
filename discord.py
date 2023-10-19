import nextcord
from nextcord.ext import commands
import config
import os
import sqlite3

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("q"),
    intents=nextcord.Intents.all(),
    help_command=None)






@bot.event
async def on_ready():
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Logged in as: {bot.user.name}")
        print(f"ID: {bot.user.id}")
    

base_dir = os.path.dirname(os.path.abspath(__file__))
cogs_dir = os.path.join(base_dir, 'cogs')
for root, dirs, files in os.walk(cogs_dir):
    for filename in files:
        if filename.endswith('.py'):
            full_path = os.path.join(root, filename)
            module_name = os.path.relpath(full_path, base_dir)
            module_name = module_name.replace(os.path.sep, '.')[:-3]

            try:
                bot.load_extension(module_name)
            except Exception as e:
                print(f"Failed to load extension {module_name}: {e}")

bot.run(config.TOKEN)
