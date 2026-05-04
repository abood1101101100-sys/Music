import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
import config

bot = Client(
    "MusicBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

assistant = Client(
    "Assistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.STRING_SESSION
)

call_py = PyTgCalls(assistant)

async def start_bot():
    print("🚀 جاري تشغيل السورس...")
    await bot.start()
    await assistant.start()
    await call_py.start()
    print("✅ السورس يعمل الآن!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
