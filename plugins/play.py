from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from yt_dlp import YoutubeDL
from pytgcalls.types import AudioPiped
from main import call_py

ytdl = YoutubeDL({"format": "bestaudio", "quiet": True})

@Client.on_message(filters.command("play") & filters.group)
async def play_handler(client, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("ارسل اسم الأغنية، مثال: /play سورة البقرة")

    m = await message.reply("🔍 جاري البحث...")
    try:
        info = ytdl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
        title = info['title']

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("⏸ إيقاف", callback_data="pause"),
             InlineKeyboardButton("▶ استئناف", callback_data="resume")],
            [InlineKeyboardButton("⏹ مغادرة", callback_data="stop")]
        ])

        await call_py.join_group_call(message.chat.id, AudioPiped(url))
        await m.edit(f"🎶 جاري تشغيل: **{title}**", reply_markup=buttons)
    except Exception as e:
        await m.edit(f"❌ خطأ: {e}")
