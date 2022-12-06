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

   


@client.event
async def on_ready():
    counter = 0
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    channel = client.get_channel(1049636120444538880)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    #init check if highscore list is there
    async for msg in channel.history(limit=200):
        if msg.author == client.user:
            counter +=1
            print(f'Nachricht Nr.{counter}: {msg.content}\n')
    
    if counter > 0:
        print(f'Anzahl der Nachrichten: {counter} \n')
    else:
        await channel.send(content='meine erste Nachricht durch code')

    #init create 4 threads
    if len(channel.threads) == 0:
       for threadName in ['Waking Shores', 'Ohn\'ahran Plains', 'Azure Span', 'Thaldaszus']:
            await channel.create_thread(name=threadName)
            print(f'created Thread {threadName}\n')
    else:
        print(f'all thread are already created')



client.run(TOKEN)