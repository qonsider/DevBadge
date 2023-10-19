import nextcord
from nextcord.ext import commands
import os
import sqlite3


class Badge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(name="badge")
    async def badge(self, inter:nextcord.Interaction):
        await inter.send("your badge in 24 hours will be claimable")
        
def setup(bot):
    bot.add_cog(Badge(bot))