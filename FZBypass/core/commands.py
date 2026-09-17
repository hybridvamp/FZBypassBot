from FZBypass import Config

SUFFIX = Config.CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f"start{SUFFIX}"
        self.BypassCommand = [f"bypass{SUFFIX}", f"bp{SUFFIX}"]
        self.LogCommand = f"log{SUFFIX}"
        self.StatsCommand = f"stats{SUFFIX}"
        self.HelpCommand = f"help{SUFFIX}"
        self.RestartCommand = f"restart{SUFFIX}"
        self.BashCommand = f"bash{SUFFIX}"
        self.ShellCommand = f"shell{SUFFIX}"

    @property
    def ExecCommands(self):
        return [self.BashCommand, self.ShellCommand]


BotCommands = _BotCommands()
