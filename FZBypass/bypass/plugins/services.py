from html import escape
from wzgram.filters import command, user, regex
from wzgram.types import InlineKeyboardButton, InlineKeyboardMarkup

from FZBypass import Config, Bypass, LOGGER
from FZBypass.core.commands import BotCommands

LOG_FILE = "log.txt"
MAX_DISPLAY = 3500


@Bypass.on_message(command(BotCommands.LogCommand) & user(Config.OWNER_ID))
async def send_logs(client, message):
    uid = message.from_user.id
    await message.reply_document(
        LOG_FILE,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Log Disp", callback_data=f"log {uid} disp"),
                    InlineKeyboardButton("Close", callback_data=f"log {uid} close"),
                ]
            ]
        ),
    )


def tg_len(text):
    """Length Telegram counts: UTF-16 code units, so an emoji costs 2."""
    return len(text.encode("utf-16-le")) // 2


def tail_lines(content, limit=MAX_DISPLAY):
    res, total = [], 0
    for line in reversed(content.splitlines()):
        parts = line.split("] [", 1)
        line = f"[{parts[1]}" if len(parts) > 1 else line
        line = line[-limit:]
        if tg_len(line) > limit:
            line = line[-(limit // 2) :]
        res.append(line)
        total += tg_len(line) + 1
        if total > limit:
            break
    res.reverse()
    while sum(tg_len(l) + 1 for l in res) > limit and len(res) > 1:
        res.pop(0)
    return res


@Bypass.on_callback_query(regex(r"^log "))
async def log_cb(client, query):
    _, owner, action = query.data.split()
    message = query.message
    uid = query.from_user.id
    if uid != int(owner):
        return await query.answer("Not Yours!", show_alert=True)

    if action == "close":
        await query.answer()
        return await message.delete()

    await query.answer("Fetching Log..")
    try:
        with open(LOG_FILE, encoding="utf-8", errors="replace") as f:
            lines = tail_lines(f.read())
        body = escape("\n".join(lines))
        await message.reply(
            f"<b>Showing Last {len(lines)} Lines from {LOG_FILE}:</b>\n\n"
            f"----------<b>START LOG</b>----------\n\n"
            f"<blockquote expandable>{body}</blockquote>\n"
            f"----------<b>END LOG</b>----------",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Close", callback_data=f"log {uid} close")]]
            ),
        )
        await message.edit_reply_markup(None)
    except Exception as e:
        LOGGER.error(f"TG Log Display: {e}")
