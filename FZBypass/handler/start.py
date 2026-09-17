from time import time
from wzgram.filters import command
from wzgram.types import InlineKeyboardButton, InlineKeyboardMarkup

from FZBypass import Bypass, BOT_START
from FZBypass.core.bot_utils import convert_time
from FZBypass.core.commands import BotCommands


@Bypass.on_message(command(BotCommands.StartCommand))
async def start_msg(client, message):
    await message.reply(
        f"""<b><i>FZ Bypass Bot!</i></b>
    
    <i>A Powerful Elegant Multi Threaded Bot written in Python... which can Bypass Various Shortener Links, Scrape links, and More ... </i>
    
    <i><b>Bot Started {convert_time(time() - BOT_START)} ago...</b></i>

🛃 <b>Use Me Here :</b> @CyberPunkGrp <i>(Bypass Topic)</i>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🎓 Dev", url="https://t.me/SilentDemonSD"),
                    InlineKeyboardButton(
                        "🔍 Deploy Own",
                        url="https://github.com/rjriajul/FZBypassBot",
                    ),
                ]
            ]
        ),
    )
