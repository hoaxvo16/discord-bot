from discord.ext.commands import Context


def log_command(ctx: Context) -> None:
    print(f"Execute cmd {ctx.command.name} from user {ctx.message.author} in channel {ctx.message.channel}")
