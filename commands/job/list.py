from .job import job
from discord.commands import Option

@job.subcommand(name="list", description="Zeigt eine Liste der Jobs")
async def job_list(ctx, category: Option(str, "Die Kategorie der Jobs", required=False)):
    # Deine Logik hier
    if category:
        await ctx.respond(f"Hier ist die Liste der Jobs für die Kategorie: {category}")
    else:
        await ctx.respond("Hier ist die gesamte Liste der Jobs!")

