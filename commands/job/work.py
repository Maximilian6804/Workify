from .job import job

@job.command(name="work", description="Arbeitet in deinem aktuellen Job")
async def job_work(ctx):
    await ctx.respond("Du hast erfolgreich gearbeitet und 100 Coins verdient!")
