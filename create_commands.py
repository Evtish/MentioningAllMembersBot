from pyrogram import Client, idle
from pyrogram.types import BotCommand

bot = Client('mentioning_all_members')

commands = [BotCommand('all', 'Mentioning all members'), BotCommand('info', 'Information about the bot')]

bot.start()
bot.set_bot_commands(commands)
idle()
bot.stop()