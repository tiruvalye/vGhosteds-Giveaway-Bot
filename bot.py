import nextcord
from nextcord.ext import commands
import config
import traceback
import time

intents = nextcord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print(f'Bot is ready.')

# Global check to ensure only users with the required role can use commands
@bot.check
async def globally_check_roles(ctx):
    user_roles = [role.id for role in ctx.author.roles]
    if config.giftmod_role_id in user_roles:
        return True
    await ctx.send("You do not have the required permissions to use this command.")
    return False

# Error handler to catch and log traceback errors
@bot.event
async def on_command_error(ctx, error):
    # Get the channel to log errors
    log_channel = bot.get_channel(config.giftlogs_channel_id)
    
    # Format the traceback error
    error_message = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
    formatted_error = f"<t:{int(time.time())}:F>\n```traceback\n{error_message}\n```"
    
    # Send the formatted error to the log channel
    if log_channel:
        await log_channel.send(formatted_error)
    else:
        print("Log channel not found. Printing error to console.")
        print(formatted_error)

# Log command usage
@bot.event
async def on_command(ctx):
    log_channel = bot.get_channel(config.giftlogs_channel_id)
    timestamp = int(time.time())
    message = f"<t:{timestamp}:F> <@{ctx.author.id}> issued command `{ctx.message.content}` in <#{ctx.channel.id}>."
    if log_channel:
        await log_channel.send(message)
    else:
        print("Log channel not found. Printing command usage to console.")
        print(message)

# Load the hello cog
bot.load_extension('cogs.hello')

bot.run(config.BOT_TOKEN)