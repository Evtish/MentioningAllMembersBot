from pyrogram import Client

api_id = 18195250
api_hash = '85086b4d8737eda59d4e7704011c699d'
bot_token = '6137687388:AAFX_FDuYab5SzxqYOpVGemBwbmmle1LcoM'
session_name = 'mentioning_all_members_bot'

app = Client(
    name=session_name,
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

app.run()