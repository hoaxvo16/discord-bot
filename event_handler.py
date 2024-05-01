import os
from discord import VoiceProtocol, FFmpegPCMAudio
from discord.ext.commands import Context
from pytube import YouTube, Stream
from command_config import command_config
from logger import log_command


async def play_audio(ctx: Context) -> None:
    log_command(ctx)
    command: str = ctx.command.name
    voice_client: VoiceProtocol = ctx.voice_client
    file_path: str = get_file_path(command)
    if os.path.isfile(file_path):
        source: FFmpegPCMAudio = FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=file_path)
        voice_client.play(source)
        return
    download_audio_from_youtube(command)
    source: FFmpegPCMAudio = FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=file_path)
    voice_client.play(source)


def download_audio_from_youtube(command: str):
    youtube_url: str | None = get_ytb_url(command)
    if youtube_url is None:
        print("Cannot get ytb url for download")
        return

    print("Downloading video from yt....")
    yt: YouTube = YouTube(get_ytb_url(command))
    audio_stream: Stream = yt.streams.filter(only_audio=True).first()  # Choose best audio

    file_name: str = get_file_name(command)
    media_path: str = get_media_path()

    audio_stream.download(output_path=media_path, filename=file_name)
    print("Downloaded video from yt")


def get_file_name(cmd: str) -> str:
    return cmd + ".mp3"


def get_file_path(cmd: str) -> str:
    return get_media_path() + "/" + get_file_name(cmd)


def get_media_path() -> str:
    return os.path.abspath(os.getcwd()) + "/media"


def get_ytb_url(cmd: str) -> str | None:
    return command_config.get(cmd)


async def play_from_resource(ctx: Context):
    log_command(ctx)
    voice_client: VoiceProtocol = ctx.voice_client
    if not voice_client:
        await ctx.send("**I am not connected to a voice channel!**")
        return

    source: FFmpegPCMAudio = FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=f'resource/{ctx.command}.mp3')
    voice_client.volume = 80
    voice_client.play(source)


async def get_list_command_available_from_resource(ctx: Context):
    files_name = os.listdir('resource')
    list_commands = ['!' + item.replace('.mp3', '') for item in files_name]
    await ctx.send("List Commands Available:")
    for command in list_commands:
        await ctx.send(command)
    await ctx.send('==============END==========')
