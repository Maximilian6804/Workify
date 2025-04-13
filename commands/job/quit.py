from .job import job

@job.command(name="quit", description="Kündigt deinen aktuellen Job")
async def job_quit(ctx):
    await ctx.respond("Du hast deinen Job gekündigt.")
