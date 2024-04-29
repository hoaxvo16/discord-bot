import os

from discord import Intents, VoiceChannel, VoiceClient, VoiceProtocol
from discord.ext import commands
from discord.ext.commands import Bot, Context
from dotenv import load_dotenv
from typing import Final

from event_handler import play_audio
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


@bot.command(pass_context=True)
async def leave(ctx: Context):
    log_command(ctx)
    voice_client: VoiceProtocol = ctx.voice_client
    await voice_client.disconnect(force=True)


@bot.command(pass_context=True)
async def gayban(ctx: Context):
    await play_audio(ctx)


bot.run(token=TOKEN)
