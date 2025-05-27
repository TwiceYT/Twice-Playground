import nextcord
from nextcord.ext import commands, application_checks
import sqlite3
import os
from dotenv import load_dotenv, dotenv_values

# Database file
load_dotenv(dotenv_path='config\config.env')
DBFile = os.getenv("DATABASE_FILE")
database = sqlite3.connect(DBFile)
cursor = database.cursor()
GuildID = os.getenv("ServerID")

intents = nextcord.Intents.all()

class Hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="hello", description="Says hello to the user", guild_ids=[int(GuildID)])
    async def hello(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.mention}!")

def setup(bot: commands.Bot):
    print("Hello Cog Registered")
    bot.add_cog(Hello(bot))