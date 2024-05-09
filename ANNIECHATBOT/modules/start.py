import asyncio
import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.enums import ChatType

from ANNIECHATBOT import app
from ANNIECHATBOT.database.chats import add_served_chat
from ANNIECHATBOT.database.users import add_served_user
from ANNIECHATBOT.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
)

# Command handler for /help
@app.on_cmd("help")
async def help_command_handler(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_video(
            video=random.choice(ANNIE_VID),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_video(
            video=random.choice(ANNIE_VID),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


