import discord
from discord.ext import commands
from discord.commands import slash_command
import json
import os

DATA_FILE = "commands/user_money.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

class Money(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Zeigt deinen Kontostand an")
    async def money(self, ctx):
        user_id = str(ctx.author.id)
        data = load_data()
        money = data.get(user_id, {}).get("money", 0)
        formatted_money = f"{money:,}".replace(",", ".")
        await ctx.respond(f"💰 Du hast aktuell **{formatted_money} €**")


def setup(bot):
    bot.add_cog(Money(bot))
