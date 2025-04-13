from discord.commands import SlashCommandGroup

job = SlashCommandGroup("job", "Job bezogene Befehle")

def setup(bot):
    bot.add_application_command(job)
