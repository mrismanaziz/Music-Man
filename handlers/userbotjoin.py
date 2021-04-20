from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin grup Anda terlebih dahulu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "MusicMan"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Helper sudah ada di obrolan Anda</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>User {user.first_name} tidak bisa bergabung dengan grup! Pastikan user tidak dibanned dalam grup."
            "\n\nAtau tambahkan secara manual @botmusikman ke Grup Anda dan coba lagi</b>",
        )
        return
    await message.reply_text(
            "<b>Helper userbot bergabung dengan obrolan Anda</b>",
        )
