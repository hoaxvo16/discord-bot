import os

from discord import Intents, VoiceChannel, VoiceClient, VoiceProtocol
from discord.ext import commands
from discord.ext.commands import Bot, Context
from dotenv import load_dotenv
from typing import Final

from event_handler import play_audio, get_list_command_available_from_resource, play_from_resource
from logger import log_command

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_BOT_TOKEN")
intents: Intents = Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.voice_states = True

bot: Bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot ready')


@bot.command(pass_context=True)
async def join(ctx: Context):
    log_command(ctx)
    voice_channel: VoiceChannel = ctx.author.voice.channel
    await voice_channel.connect()
    await get_list_command_available_from_resource()


@bot.command(pass_context=True)
async def leave(ctx: Context):
    log_command(ctx)
    voice_client: VoiceProtocol = ctx.voice_client
    await voice_client.disconnect(force=True)


@bot.command(pass_context=True)
async def gayban(ctx: Context):
    await play_audio(ctx)


@bot.command(pass_context=True)
async def locc(ctx: Context):
    await play_audio(ctx)


@bot.command(pass_context=True)
async def dmcuocdoi(ctx: Context):
    await play_audio(ctx)


@bot.command(pass_context=True)
async def anhemcc(ctx: Context):
    await play_audio(ctx)

@bot.command()
async def next_level(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def oy(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def chana(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def ua(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def cuutui(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def yamate(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def ghechua(ctx: Context):
    await play_from_resource(ctx)
@bot.command()
async def dmdoi(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def baymuoi(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def fb(ctx: Context):
    await play_from_resource(ctx)

@bot.command()
async def dbk(ctx: Context):
    await play_from_resource(ctx)


bot.run(token=TOKEN)
