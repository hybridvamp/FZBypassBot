from wzgram.filters import command
from wzgram.types import InlineKeyboardButton, InlineKeyboardMarkup

from FZBypass import Bypass
from FZBypass.core.commands import BotCommands


@Bypass.on_message(command(BotCommands.StartCommand))
async def start_msg(client, message):
    await message.reply(
        f"""<b><i>FZ Bypass Bot!</i></b>

<i>A Powerful Elegant Multi Threaded Bot written in Python... which can Bypass Various Shortener Links, Scrape links, and More ... </i>

📖 <b>Commands :</b> /{BotCommands.HelpCommand}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔍 Deploy Own",
                        url="https://github.com/rjriajul/FZBypassBot",
                    ),
                ]
            ]
        ),
    )
