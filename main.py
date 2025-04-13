import os
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ist nun Hochgefahren!")

# Erweiterter Loader – lädt nur Top-Level-Dateien und __init__.py aus Unterordnern
def recursive_load(bot, path, base_module, top_level=True):
    for entry in os.scandir(path):
        if entry.is_dir():
            # Nur __init__.py wird als Extension geladen
            init_path = os.path.join(entry.path, '__init__.py')
            if os.path.isfile(init_path):
                module_name = f"{base_module}.{entry.name}"
                bot.load_extension(module_name)
            # Tiefer gehen, aber keine weiteren .py-Dateien laden
            recursive_load(bot, entry.path, f"{base_module}.{entry.name}", top_level=False)
        elif entry.is_file() and entry.name.endswith('.py') and entry.name != "__init__.py":
            if top_level:
                module_name = f"{base_module}.{entry.name[:-3]}"
                bot.load_extension(module_name)

if __name__ == "__main__":
    for category in ['commands']:
        if os.path.exists(f'./{category}'):
            recursive_load(bot, f'./{category}', category)

load_dotenv()
token = os.getenv("TOKEN")
if not token:
    print("Fehler: TOKEN wurde nicht geladen. Überprüfe deine .env-Datei!")
    exit(1)

bot.run(token)
