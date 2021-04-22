from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo 👋! Saya dapat memutar musik dalam obrolan suara Grup Telegram.\n\n✣ Apakah Anda ingin saya memutar musik di obrolan suara grup Telegram Anda? Silakan klik \'📜 Panduan Menggunakan BOT 📜\' tombol di bawah untuk mengetahui bagaimana cara menggunakan saya.\n\n✣ Tambahkan [Assistant Music Player](https://t.me/GB_Assistant) ke grup Anda untuk memutar musik di obrolan suara grup Anda.\n\n✣ Info & perintah selengkapnya yang disebutkan di [User Manual](https://telegra.ph/GB--MUSIC-PLAYER-04-22)\n\nManaged With ☕️ By [ɢᴏᴏᴅ ʙᴏʏs](https://t.me/GB_03101999)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Panduan Menggunakan BOT 📜", url="https://telegra.ph/GB--MUSIC-PLAYER-04-22")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/SharingUserbot"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/Lunatic0de"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✣ Pemutar Musik Sedang Online ✣**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/SharingUserbot"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/GB_03101999"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/SharingUserbot"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/GB_03101999"
                    )
                ]
            ]
        )
   )
