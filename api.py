import discord
from aiohttp import ClientSession
from discord.ext import commands,tasks

class API(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

    @commands.command(
      name ="stocks",
      description ="shows stock price from yahoo finance"
    )
    async def stocks(self, ctx):
      url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

      headers={
        'x-rapidapi-key': "a462edae62msh505ff93a62af7b0p15813ajsn41b41771d1e9",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
      }

      async with ClientSession() as session:
        async with session.get(url, headers=headers) as response:
          r = await response.json()
          print(r)
          await ctx.send(['message'])

def setup(bot):
  bot.add_cog(API(bot))

