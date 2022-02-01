import discord
import os
import nacl
from discord.ext import commands,tasks
from dotenv import load_dotenv
import youtube_dl

client = discord.Client()
token = open("/Users/delracman/Documents/Discord/token.txt","r") # tokens in .gitignore token.txt file
d_api_key = token.readline()
token.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    # prints the username of the user who used the !user command
    if msg.startswith("!user"):
        await message.channel.send(message.author)
        #print(message.author.voice.channel)

    # makes bot join channel user is currently in
    #TODO: add command for setting default channel (right now message is just sent)
    if msg.startswith("!join"):
        if message.author.voice is None:
            await message.channel.send("Please join a channel, and then make me join")
        else:
            voice = discord.utils.get(client.voice_clients)

            #joins channel if not already in channel
            if voice is None:
                destination = message.author.voice.channel
                vc = await destination.connect()
            # disconnects from current channel and joins new channel
            else:
                for vc in client.voice_clients:
                    if vc.guild == message.guild:
                        await vc.disconnect()
                destination = message.author.voice.channel
                vc = await destination.connect()

    if msg.startswith("!leave"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                await vc.disconnect()

        print(response)

    #if msg.startswith("$inspire"):
        #quote = get_quote()
        #await message.channel.send(quote)

client.run(d_api_key)


'''

load_dotenv()

token = open("/Users/delracman/Documents/Discord/token.txt","r") # tokens in .gitignore token.txt file
DISCORD_TOKEN = token.read()
token.close()

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "general" :
                await channel.send('Bot Activated..')
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()
            
@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='play', help='To play song')
async def play(ctx,url):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

if __name__ == "__main__" :
    bot.run(DISCORD_TOKEN)'''




