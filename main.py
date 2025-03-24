import discord
from discord.ext import commands, tasks
import time
from colorama import Fore, init

bot = commands.Bot(command_prefix='<>', intents=discord.Intents.all())

@bot.event
async def on_ready():

    print('-----------------------------Logging in----------------------------------------')
    print(Fore.GREEN + f"Logged in as {bot.user}" + Fore.RESET)
    print(Fore.GREEN + 'Welcome to Bot-Main. Made by coder-boner on GitHub!' + Fore.RESET)
    #print('------------------------------Syncing commands---------------------------------------')

    # Track the start time of the bot
    global start_time
    start_time = time.time()
    update_uptime.start()  # Start the uptime task


@tasks.loop(seconds=1)
async def update_uptime():
    # Calculate the bot's uptime
    uptime_seconds = int(time.time() - start_time)

    # Calculate time components
    years = uptime_seconds // (365 * 24 * 60 * 60)
    uptime_seconds %= (365 * 24 * 60 * 60)
    months = uptime_seconds // (30 * 24 * 60 * 60)
    uptime_seconds %= (30 * 24 * 60 * 60)
    weeks = uptime_seconds // (7 * 24 * 60 * 60)
    uptime_seconds %= (7 * 24 * 60 * 60)
    days = uptime_seconds // (24 * 60 * 60)
    uptime_seconds %= (24 * 60 * 60)
    hours = uptime_seconds // (60 * 60)
    uptime_seconds %= (60 * 60)
    minutes = uptime_seconds // 60
    seconds = uptime_seconds % 60

    # Format the uptime string
    uptime_string = f"{years}Y {months}M {weeks}W {days}D {hours}H {minutes}M {seconds}S"

    # Update the bot's presence with the formatted uptime
    await bot.change_presence(activity=discord.Game(name=uptime_string))

# Run the bot
bot.run("TOKEN")
