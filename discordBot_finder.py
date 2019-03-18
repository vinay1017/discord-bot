import discord
import urllib.request
from bs4 import BeautifulSoup
import re
import cathy
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

# client = discord.Client()
client = commands.Bot(command_prefix='!')
# bot = commands.Bot(command_prefix='.')

def importfile(file):
    if str(file).__contains__("txt"):
        importedfile = open(file, "r")
        importedfile = importedfile.read()
    return importedfile


TOKEN = str(importfile('cache/token.txt'))  # put your token here.
# print('token used' + TOKEN)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(pass_context=True)
async def join(ctx):
    #author = ctx.message.author
    #channel = ctx.message.author.voice.voice_channel
    #await bot.join_voice_channel(channel)
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    #await client.join_voice
    print("Bot joined vc")

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    # voice client = instance of the bot being in voice channel
    await voice_client.disconnect()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('hello') or message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('hi') or message.content.startswith('Hi'):
        msg = 'What is my purpose {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('hello VinayJunior'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('should you vote for Roche') or message.content.startswith('should Roche'):
        msg = 'No. {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Thank you, Vinay') or message.content.startswith('thank you, vinay'):
        msg = 'You are welcome. {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('you pass butter'):
        msg = 'oH mY gOD https://tenor.com/view/rick-and-morty-you-pass-butter-welcome-to-the-club-gif-9281996 {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('bring me') or message.content.startswith('Bring me'):
        if "bring me a beer" in message.content:
            msg = 'okay dad 🍺'.format(message)
            await client.send_message(message.channel, msg)
        else:
            msg = 'no'.format(message)
            await client.send_message(message.channel, msg)
    # if str(message.content.startswith('you pass butter')).__contains__():

    # YouTube method
    if message.content.startswith('find'):
        # could make a txt log of commands? write txt file.
        print(message.content)  # this is how you get user message
        userString = message.content
        userStringSize = len(userString)  # works
        userString = userString[5:userStringSize]
        print(userString)

        # how to find single videos:
        query_string = urllib.parse.urlencode({"search_query": userString})  # input
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        print("http://www.youtube.com/watch?v=" + search_results[0])

        videoString = "http://www.youtube.com/watch?v=" + search_results[0]

        # videoString = '' #this would be whatever the youtube search finds.
        msg = 'here is your video: ' + videoString + ' ' + '{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    # Google method
    if message.content.startswith('google') or message.content.startswith('Google'):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")

        userString = message.content
        userStringSize = len(userString)  # works
        userString = userString[7:userStringSize]
        print(userString)
        # to search
        query = userString

        for j in search(query, tld="co.in", num=10, stop=1, pause=2):
            print(j)
            messagej = j
            msg = 'here is the top search result: ' + j + ' ' + '{0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)



# main
client.run(TOKEN)
