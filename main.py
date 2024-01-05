from pyrogram import Client, filters, enums
#from create_session import session_name

bot = Client('mentioning_all_members')

with open('info.txt', encoding='utf-8') as info_file:
    info_text = info_file.read()


@bot.on_message(filters.command('all'))
async def get_all_members(client, message):
    if message.chat.type == enums.ChatType.GROUP or message.chat.type == enums.ChatType.SUPERGROUP:
        members = []
        chat_id = message.chat.id
        sender_username = message.from_user.username

        async for member in bot.get_chat_members(chat_id):
            curr_username = member.user.username
            if not member.user.is_bot and curr_username != sender_username:
                members.append('@' + curr_username)

        await bot.send_message(chat_id, ' '.join(members), reply_to_message_id=message.reply_to_message_id)

    else:
        await bot.send_message(message.chat.id, 'Эта команда предназначена только для групп')


@bot.on_message(filters.command('info'))
async def info(client, message):
    await bot.send_message(message.chat.id, info_text)


@bot.on_message(filters.command('skibidi'))
async def info(client, message):
    await bot.send_message(message.chat.id, 'брр скибиди доп доп доп ес ес')


bot.run()