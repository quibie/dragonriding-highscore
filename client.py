#bot

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(command_prefix='!', intents=intents)

RacesWakingShore = """Advanced | Apex Canopy River Run / Flusslauf des Hohen Blätterdachs
Advanced | Emberflow Flight / Glutstrom-Flug
Advanced | Flashfrost Flyover / Blitzfrost-Überflug
Advanced | Ruby Lifeshrine Loop / Rubinlebensschrein-Schleife
Advanced | Uktulut Coaster / Uktuluter Küstenachter
Advanced | Wild Preserve Circuit / Wildreservat-Überflug
Advanced | Wild Preserve Slalom / Wildreservat-Slalom
Advanced | Wingrest Roundabout / Schwingenrastkreisel
Basic | Apex Canopy River Run / Flusslauf des Hohen Blätterdachs
Basic | Emberflow Flight / Glutstrom-Flug
Basic | Flashfrost Flyover / Blitzfrost-Überflug
Basic | Ruby Lifeshrine Loop / Rubinlebensschrein-Schleife
Basic | Uktulut Coaster / Uktuluter Küstenachter
Basic | Wild Preserve Circuit / Wildreservat-Überflug
Basic | Wild Preserve Slalom / Wildreservat-Slalom
Basic | Wingrest Roundabout / Schwingenrastkreisel""".splitlines()


TestRaceString = """1. Platz: \"Rainaa | Johann\"\t - 13,37 Sekunden
2. Platz: \"Djarin | Paddy\"\t - 14,45 Sekunden
3. Platz:
4. Platz:
5. Platz:"""
class race:
    #the race class to track the times and create the message
    def __init__(self, raceList, location):
        self.loc = location
        self.top5 = raceList.splitlines()
        for i in range(5):
            self.top5[i] = self.top5[i][10:]


@client.event
async def on_ready():
    #get configuired guild
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    channel = client.get_channel(int(os.getenv('CHANNEL_ID')))
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    #init check if highscore list is there
    for location in channel.threads:
        counter = 0
        async for msg in location.history(limit=200):
            if msg.author == client.user:
                counter +=1
                print(f'Nachricht Nr.{counter}: {msg.content}\n')
        if counter > 0:
            print(f'Anzahl der Nachrichten: {counter} \n')
        else:
            await location.send(content='meine erste Nachricht durch code')

    #init create 4 threads
    if len(channel.threads) == 0:
       for threadName in ['Waking Shores', 'Ohn\'ahran Plains', 'Azure Span', 'Thaldaszus']:
            await channel.create_thread(name=threadName,type=discord.ChannelType.public_thread)
            print(f'created Thread {threadName}\n')
    else:
        print(f'all thread are already created')


    TestRace = race(TestRaceString, "Discord Schleife")

    print(f'{TestRace.top5}\n')


client.run(TOKEN)