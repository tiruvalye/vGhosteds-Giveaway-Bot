from nextcord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Hello, <@{ctx.author.id}>! I'm **online** and my bot.py file is functioning.")

def setup(bot):
    bot.add_cog(Hello(bot))