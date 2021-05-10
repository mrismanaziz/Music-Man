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


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> ☬ Hai {message.from_user.first_name} welcome to 𝑭𝑯 𝑴𝑼𝑺𝑰𝑲 ☬\n
𝑭𝑯 𝑴𝑼𝑺𝑰𝑲 adalah Bot Music yang dapat memutar lagu di Voice Chat Group.
Saya memiliki fitur :
┏━━
✦҈͜͡➳ Memutar musik.
✦҈͜͡➳ Mendownload lagu.
✦҈͜͡➳ Mencari lagu yang ingin kamu putar atau Download.
┗━━
❃ Managed with by : [Ahmdrzii](https://t.me/ahmdrzii88)
❃ Thanks to : [Risman](https://t.me/mrismanaziz)

☞ Ingin menambahkan saya ke grup?
☞ Tambahkan saya dan [Musik Assistant](t.me/MusicAssistant88) ke Group kamu!
</b>""",

# Edit Yang Perlu Lu ganti 
# Tapi Jangan di Hapus Thanks To nya Yaaa :D

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Cara menggunakan BOT", url="https://t.me/Lunatic0de/20")
                  ],[
                    InlineKeyboardButton(
                        "Join Grup", url="https://t.me/gabutgabutonline"
                    ),
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/katasecangkir"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cara menggunakan BOT", url="https://t.me/Lunatic0de/20"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n✅ **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/SweetKillerBot"
                    )
                ]
            ]
        )
   )
