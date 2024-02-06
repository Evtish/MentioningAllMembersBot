from pyrogram import Client, filters, enums
#from create_session import session_name

'''proxy = {
     'scheme': 'http',
     'hostname': 'evtish.pythonanywhere.com',
     'port': 3128,
     'username': 'username',
     'password': 'password'
}

bot = Client('mentioning_all_members_bot', proxy=proxy)'''
bot = Client('mentioning_all_members_bot')

with open('info.txt', encoding='utf-8') as info_file:
    info_text = info_file.read()


@bot.on_message(filters.command('all'))
async def get_all_members(client, message):
    if message.chat.type == enums.ChatType.GROUP or message.chat.type == enums.ChatType.SUPERGROUP:
        members = []
        chat_id = message.chat.id

        '''
        printing_members = []
        is_printed = False
        async for member in bot.get_chat_members(chat_id):
            curr_username = member.user.username
            if curr_username and not member.user.is_bot and curr_username != message.from_user.username:
                if len(' '.join(printing_members)) + len(curr_username) + 2 <= 4096:
                    printing_members.append('@' + curr_username)
                else:
                    await bot.send_message(chat_id, ' '.join(printing_members), reply_to_message_id=message.reply_to_message_id)
                    printing_members = []
                    is_printed = True
        if not is_printed:
            await bot.send_message(chat_id, ' '.join(printing_members), reply_to_message_id=message.reply_to_message_id)
        '''

        async for member in bot.get_chat_members(chat_id):
            curr_username = member.user.username
            if curr_username and not member.user.is_bot and curr_username != message.from_user.username:
                members.append('@' + str(curr_username))

        while True:
            printing_members = []
            while members and len(printing_members) + len(members[0]) + 1 < 4096:
                printing_members.append(members.pop())

            await bot.send_message(chat_id, ' '.join(printing_members), reply_to_message_id=message.reply_to_message_id)

            if not members:
                break

    else:
        await bot.send_message(message.chat.id, 'Эта команда предназначена только для групп')


@bot.on_message(filters.command('info'))
async def info(client, message):
    await bot.send_message(message.chat.id, info_text)


@bot.on_message(filters.command('skibidi'))
async def skibidi(client, message):
    await bot.send_message(message.chat.id, 'брр скибиди доп доп доп ес ес')


@bot.on_message(filters.command('sigma'))
async def sigma(client, message):
    await bot.send_animation(message.chat.id, 'other files/sigma.gif')


bot.run()