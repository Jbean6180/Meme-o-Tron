import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import os, shutil
import uuid
import requests
from random import choice
import meme

cogs = [meme]

client = commands.Bot(command_prefix='?',intents = discord.Intents.all(),case_insensitive=True)


status = ['Being Sus','Osu','Dripping out']


@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Hey Daddy {member.mention}!')

@client.command(name='save', help='saves ;)')
async def save(ctx):
    # use command save in the comment box when uploading an image to save the image as a jpg
        try:
            url = ctx.message.attachments[0].url           
        except IndexError:
            print("Error: No attachments")
            await ctx.send("No attachments detected!")
        else:
            if url[0:26] == "https://cdn.discordapp.com":  
                r = requests.get(url, stream=True)
                imageName = str(uuid.uuid4()) + '.jpg'     
                with open('downloads/' + imageName, 'wb') as out_file:
                    print('Saving image: ' + imageName)
                    shutil.copyfileobj(r.raw, out_file)
                  
@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Hey Daddy']
    await ctx.send(choice(responses))

@client.command(name='sus', help='This command returns a random welcome message')
async def sus(ctx):
    responses = ['Cmon guys love songs are not that bad', 'I went to catholic school because I needed a break from girls', 'They should get a boys volleyball team at my school', 'Got banned from Xbox for watching gay porn', 'My barber just asked me “what’s your team?” and I replied “Gay” and he replied “football?” to which I replied “Oh no thank you” and now neither of us knows where to go with this mess of a convo. So now we are just sitting in silence.']
    await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['Thanks']
    await ctx.send(choice(responses))

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("DISCORD-BOT-TOKEN")






