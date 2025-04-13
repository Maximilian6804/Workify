import discord
from discord.ext import commands
from discord.commands import slash_command
import random
import time
import json
import os

DATA_FILE = "commands/user_money.json"
COOLDOWN = 6 * 60 * 60  # 6 Stunden

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

class Work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Arbeite und verdiene Geld (6h Cooldown)")
    async def work(self, ctx):
        user_id = str(ctx.author.id)
        data = load_data()
        now = time.time()

        if user_id not in data:
            data[user_id] = {"money": 0, "last_work": 0}

        last_work = data[user_id].get("last_work", 0)

        if now - last_work < COOLDOWN:
            remaining = COOLDOWN - (now - last_work)
            hours = int(remaining // 3600)
            minutes = int((remaining % 3600) // 60)
            return await ctx.respond(
                f"⏳ Du kannst in **{hours}h {minutes}min** wieder arbeiten.",
                ephemeral=True
            )

        amount = random.randint(70, 200)
        data[user_id]["money"] += amount
        data[user_id]["last_work"] = now

        save_data(data)

        formatted_amount = f"{amount:,}".replace(",", ".")
        await ctx.respond(f"💼 Du hast gearbeitet und **{formatted_amount} €** verdient!")

def setup(bot):
    bot.add_cog(Work(bot))
