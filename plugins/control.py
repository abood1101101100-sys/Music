import os
import sys
from pyrogram import Client, filters
from main import call_py
import config

@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    chat_id = query.message.chat.id
    if data == "pause":
        await call_py.pause_stream(chat_id)
        await query.answer("تم الإيقاف")
    elif data == "resume":
        await call_py.resume_stream(chat_id)
        await query.answer("تم الاستئناف")
    elif data == "stop":
        await call_py.leave_group_call(chat_id)
        await query.answer("تمت المغادرة")

@Client.on_message(filters.command("update") & filters.user(config.OWNER_ID))
async def update_bot(client, message):
    await message.reply("🔄 جاري تحديث السورس من GitHub...")
    os.system("git pull")
    os.execl(sys.executable, sys.executable, "main.py")
