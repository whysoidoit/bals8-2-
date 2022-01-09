#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Channel : <a href='https://t.me/joinchat/slPWoPDfoJc3NTVl'>♏𝗮𝗹𝗮𝘆𝗮𝗹𝗮𝗺_𝗖𝗶𝗻𝗲𝗺𝗮</a>\n○ malayalam_movies : <code>Python3</code>\n○ Library : <a href='https://t.me/joinchat/slPWoPDfoJc3NTVl'>Pyrogram asyncio {__version__}</a>\n○ Series World : <a href='https://t.me/mc_serie'>Click here</a>\n○ Channel : @MALAYAYALIES\n○ Support Group : @malayalam2</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
