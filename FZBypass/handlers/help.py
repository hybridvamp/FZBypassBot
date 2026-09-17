from wzgram.filters import command

from FZBypass import Config, Bypass
from FZBypass.core.commands import BotCommands

BYPASS_CMDS = ", ".join(f"/{c}" for c in BotCommands.BypassCommand)

HELP = f"""⌬ <b><i>FZ Bypass Bot Help :</i></b>

┎ <b><i>BYPASS :</i></b>
┠ <b>{BYPASS_CMDS}</b> <code>[link]</code>
┠ <i>Or reply to any message holding links.</i>
┖ <i>Inline :</i> <code>@{{me}} !bp [link]</code>

┎ <b><i>GENERAL :</i></b>
┠ <b>/{BotCommands.StartCommand}</b> <i>- Bot info</i>
┠ <b>/{BotCommands.HelpCommand}</b> <i>- This message</i>
┖ <b>/{BotCommands.StatsCommand}</b> <i>- Bot and system resources</i>"""

OWNER_HELP = f"""

┎ <b><i>OWNER ONLY :</i></b>
┠ <b>/{BotCommands.LogCommand}</b> <i>- Get log file</i>
┠ <b>/{BotCommands.RestartCommand}</b> <i>- Update and restart</i>
┠ <b>/{BotCommands.BashCommand}</b> <code>[code]</code> <i>- Run python</i>
┖ <b>/{BotCommands.ShellCommand}</b> <code>[cmd]</code> <i>- Run shell</i>"""

AUTO_NOTE = """

<i>AUTO_BYPASS is on, so any link you send is bypassed without a command.</i>"""


@Bypass.on_message(command(BotCommands.HelpCommand))
async def help_msg(client, message):
    text = HELP.format(me=client.me.username)
    if message.from_user.id == Config.OWNER_ID:
        text += OWNER_HELP
    if Config.AUTO_BYPASS:
        text += AUTO_NOTE
    await message.reply(text, disable_web_page_preview=True)
