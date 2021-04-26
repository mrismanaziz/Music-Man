# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo 👋! Saya dapat memutar musik dalam obrolan suara Grup Telegram.\n\n✣ Apakah Anda ingin saya memutar musik di obrolan suara grup Telegram Anda? Silakan klik \'📜 Panduan Menggunakan BOT 📜\' tombol di bawah untuk mengetahui bagaimana cara menggunakan saya.\n\n✣ Tambahkan [Assistant Mussic santai](Https://t.me/Assistenmussicsantai_bot) ke grup Anda untuk memutar musik di obrolan suara grup Anda.\n\nManaged With ☕️ By [Ramadhan](https://t.me/gksukaribett)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Panduan Menggunakan BOT 📜", url="https://telegra.ph/𝙈𝙪𝙨𝙨𝙞𝙘-𝙨𝙖𝙣𝙩𝙖𝙞-𝙗𝙤𝙩-𝙫𝙤𝙞𝙘𝙚-𝙘𝙝𝙖𝙩-𝙜𝙧𝙤𝙪𝙥-04-25")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/wavyheartt"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="Https://t.me/calonpenyanyi"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/wavyheartt"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/gksukaribett"
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
                        "Group Support", url="https://t.me/wavyheartt"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/gksukaribett"
                    )
                ]
            ]
        )
   )
