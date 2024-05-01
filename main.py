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
async def on_ready() -> None:
    print('Bot ready')


@bot.command(pass_context=True)
async def join(ctx: Context) -> None:
    log_command(ctx)
    voice_channel: VoiceChannel = ctx.author.voice.channel
    await voice_channel.connect()


@bot.command(pass_context=True)
async def leave(ctx: Context) -> None:
    log_command(ctx)
    voice_client: VoiceProtocol = ctx.voice_client
    await voice_client.disconnect(force=True)


@bot.command(pass_context=True)
async def listcmd(ctx: Context) -> None:
    log_command(ctx)
    command_names: list[str] = [command.name for command in bot.commands]
    message: str = "\n".join(command_names)
    await ctx.message.channel.send(message)


@bot.command(pass_context=True)
async def stop(ctx: Context) -> None:
    log_command(ctx)
    voice_client: VoiceProtocol = ctx.voice_client
    voice_client.stop()


@bot.command(pass_context=True)
async def gayban(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command(pass_context=True)
async def locc(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command(pass_context=True)
async def dmcuocdoi(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command(pass_context=True)
async def anhemcc(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def next_level(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def oy(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def chana(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def ua(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def cuutui(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def yamate(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def ghechua(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def dmdoi(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def baymuoi(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def fb(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def dbk(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def dongu(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def immmom(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def lauduv(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def caijzbanoi(ctx: Context) -> None:
    await play_audio(ctx)


@bot.command()
async def bocphet(ctx: Context) -> None:
    await play_audio(ctx)


bot.run(token=TOKEN)
