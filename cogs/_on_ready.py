from discord.ext import commands
import json, time, os
from ping3 import verbose_ping


def get_data():
    with open("data.json", "r") as f:
        datas = json.load(f)
    return datas

class _on_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready! ")
        print(f"Bot name: {self.bot.user}")
        print("--------------------")

        # Ping
        while 1:
            datas = get_data()
            websites = datas['website']
            for website in websites:
                verbose_ping(website)
            time.sleep(300)


def setup(bot):
	bot.add_cog(_on_ready(bot))