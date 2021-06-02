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
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from MusicMan.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("`Globally Broadcasting Msg...`")
        if not message.reply_to_message:
            await lol.edit("**Balas pesan teks apa pun untuk gcast**")
            return
        msg = message.reply_to_message.text
        for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"**Berhasil Mengirim Pesan Ke** `{sent}` **Grup, Gagal Mengirim Pesan Ke** `{failed}` **Grup**")
            except:
                failed=failed+1
                await lol.edit(f"**Berhasil Mengirim Pesan Ke** `{sent}` **Grup, Gagal Mengirim Pesan Ke** `{failed}` **Grup**")
            await asyncio.sleep(0.7)
        await message.reply_text(f"**Mengirim Pesan Ke** `{sent}` **Grup, Gagal Mengirim Pesan Ke** `{failed}` **Grup**")
