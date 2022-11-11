from discord.ext import commands
import json, discord

async def get_data():
    with open("data.json", "r") as f:
        datas = json.load(f)
    return datas

class _ping_add_del(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping_add(ctx, web):
        datas = await get_data()
        # users_id_list = datas['users_id']
        if str(web).__contains__("https://"):
            datas['website'].append(str(web))
            em = discord.Embed(
                title="Done! ", 
                description="Website has added into list! ", 
                color=discord.Color.blue,
            )
            await ctx.reply(embed=em)
        else:
            em = discord.Embed(
                title="Error!", 
                description="Website doesn't contain `https://`. Check your link.", 
                color=discord.Color.red,
            )
            await ctx.reply(embed=em)

        with open("data.json", "w") as f:
            json.dump(datas, f)

    @commands.command()
    async def ping_del(ctx, web):
        datas = await get_data()
        # users_id_list = datas['users_id']
        if str(web).__contains__("https://"):
            try:
                datas['website'].remove(str(web))
                em = discord.Embed(
                    title="Done! ", 
                    description="Website has added into list! ", 
                    color=discord.Color.blue,
                )
                await ctx.reply(embed=em)
            except:
                em = discord.Embed(
                    title="Error! ", 
                    description=f"Website no found in list! \nList: {datas['website']}", 
                    color=discord.Color.red,
                )
                await ctx.reply(embed=em)
        else:
            em = discord.Embed(
                title="Error!", 
                description="Website doesn't contain `https://`. Check your link.", 
                color=discord.Color.red,
            )
            await ctx.reply(embed=em)

        with open("data.json", "w") as f:
            json.dump(datas, f)


def setup(bot):
	bot.add_cog(_ping_add_del(bot))