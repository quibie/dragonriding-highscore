#bot
import dragonraces
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

Lraces = dragonraces.Races


TestRaceString = """1. Platz: \"Rainaa | Johann\"\t - 13,37 Sekunden
2. Platz:
3. Platz:
4. Platz:
5. Platz:"""


@bot.event
async def on_ready():
    #get configuired guild
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    
    baseChannel = bot.get_channel(CHANNEL_ID)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    #init check if highscore list is there
    for location in baseChannel.threads:
        counter = 0
        if "Shores" in location.name:
            async for msg in location.history(limit=20):
                if (msg.author == bot.user) and (any(i in Lraces[:15] for i in msg.content)):
                    return
                else:
                    for i in range(15):
                        await location.send(content=f'{Lraces[i]}\n{TestRaceString}')

        # elif "Plains" in location.name:

        # elif "Azure" in location.name:

        # elif "Thaldaszus" in location.name:

        # async for msg in location.history(limit=200):
        #     if msg.author == bot.user:
        #         counter +=1
        # if counter > 0:
        #     print(f'Anzahl der Nachrichten: {counter}')
        # else:
        #     await location.send(content='meine erste Nachricht durch code')

    #init create 4 threads
    if len(baseChannel.threads) == 0:
       for threadName in ['Waking Shores', 'Ohn\'ahran Plains', 'Azure Span', 'Thaldaszus']:
            await baseChannel.create_thread(name=threadName,type=discord.ChannelType.public_thread)
            print(f'created Thread {threadName}')
    else:
        print(f'all thread are already created')

@bot.event
async def on_message(message):
    #check for message in the configured textChannel
    if (message.channel.id != CHANNEL_ID) and (message.author == bot.user):
        return
    else:
        await bot.process_commands(message)

@bot.command()
async def race(ctx, race: int, time: float):
    print(f'LOG - Author: {ctx.author} Text: {ctx.message.content}')
    await ctx.send(content=f'Hello \"{ctx.author.nick}\". Your time for race \"{Lraces[race -1]}\" is {time} seconds')

bot.run(TOKEN)