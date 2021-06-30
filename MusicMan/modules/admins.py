# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

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


from asyncio import QueueEmpty
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from MusicMan.config import que
from MusicMan.function.admins import set
from MusicMan.helpers.channelmusic import get_chat_id
from MusicMan.helpers.decorators import authorized_users_only
from MusicMan.helpers.decorators import errors
from MusicMan.helpers.filters import command
from MusicMan.helpers.filters import other_filters
from MusicMan.services.callsmusic import callsmusic
from MusicMan.services.queues import queues


@Client.on_message(filters.command("reload"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        (
            member.user
            for member in await message.chat.get_members(
                filter="administrators"
            )
        ),
    )

    await message.reply_text("✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/SharingUserbot"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/mrismanaziz"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "paused"
    ):
        await message.reply_text("❗ **Tidak ada Lagu yang sedang diputar!**")
    else:
        callsmusic.pause(chat_id)
        await message.reply_text("▶️ **Paused!**")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "playing"
    ):
        await message.reply_text("❗ **Tidak ada Lagu yang sedang dijeda!**")
    else:
        callsmusic.resume(chat_id)
        await message.reply_text("⏸ **Resumed!**")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ **Tidak ada Lagu yang sedang diputar!**")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        await callsmusic.stop(chat_id)
        await message.reply_text("❌ **Memberhentikan Lagu!**")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ **Tidak ada Lagu Selanjutnya untuk dilewati!**")
    else:
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            await callsmusic.stop(chat_id)
        else:
            await callsmusic.set_stream(
                chat_id, 
                queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- Melewati Lagu **{skip[0]}**\n- Sekarang Memutar Lagu **{qeue[0][0]}**")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(
                filter="administrators"
            )
        ),
    )

    await message.reply_text("✅️ **Daftar admin** telah **diperbarui**")
