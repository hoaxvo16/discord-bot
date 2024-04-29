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

    yt: YouTube = YouTube(get_ytb_url(command))
    audio_stream: Stream = yt.streams.filter(only_audio=True).first()  # Choose best audio

    file_name: str = get_file_name(command)
    media_path: str = get_media_path()

    audio_stream.download(output_path=media_path, filename=file_name)


def get_file_name(cmd: str) -> str:
    return cmd + ".mp3"


def get_file_path(cmd: str) -> str:
    return get_media_path() + "/" + get_file_name(cmd)


def get_media_path() -> str:
    return os.path.abspath(os.getcwd()) + "/media"


def get_ytb_url(cmd: str) -> str | None:
    return command_config.get(cmd)
