import discord
from discord.ext import commands
import requests
import aiohttp
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)
SERVER_ID = 930591458682081301
def generate_price_embed(current_price, price_changes):
    embed = discord.Embed(
        title="Mistery Mery Price",
        description=f"The current price of Mery is ${current_price:.8f}",
        color=0x00ff00 if price_changes['h1'] >= 0 else 0xff0000
    )
    embed.add_field(
        name="1hr Change",
        value=f"{price_changes['h1']}%"
    )
    embed.add_field(
        name="6hr Change",
        value=f"{price_changes['h6']}%"
    )
    embed.add_field(
        name="24hr Change",
        value=f"{price_changes['h24']}%"
    )
    return embed
async def check_message_for_price(message):
    if 'mery' in message.content.lower() and 'price' in message.content.lower():
        return True
    if 'mistery' in message.content.lower() and 'price' in message.content.lower():
        return True
    return False
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if await check_message_for_price(message):
        url = 'https://api.dexscreener.com/latest/dex/pairs/cronos/0xA51231984ff01F4933a9FA24E8fd143f18ae6772'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            current_price = float(data['pairs'][0]['priceUsd'])
            price_changes = data['pairs'][0]['priceChange']
            embed = generate_price_embed(current_price, price_changes)
            sent_message = await message.channel.send(embed=embed)
            
            guild = bot.get_guild(SERVER_ID)
            if guild:
                me = guild.me
                new_nickname = f"${current_price:.8f}"
                await me.edit(nick=new_nickname)
        else:
            embed = discord.Embed(
                title="Error",
                description="Unable to fetch the price for Mery.",
                color=0xff0000  # Red color
            )
            sent_message = await message.channel.send(embed=embed)
            await sent_message.delete(delay=120)

    await bot.process_commands(message)
bot.run('MERY_BOT_TOKEN')
