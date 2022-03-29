from colored import stylize
from datetime import datetime
import colored


class Logger:
    def __init__(self, title, id_num=None):
        if id_num is None:
            self.identifier = "[{}]".format(title)
        else:
            self.identifier = "[{} {}]".format(title, id_num)

    def generate_text(self, identifier, tag, msg):
        current_time = datetime.now().strftime("%I:%M:%S.%f %p")
        return f"[{current_time}] {identifier} [{tag}] -> {msg}"

    def alert(self, msg, tag="ALERT"):
        text = self.generate_text(self.identifier, tag, msg)
        print(stylize(text, colored.fg("magenta")), flush=True)

    def info(self, msg, tag="INFO"):
        text = self.generate_text(self.identifier, tag, msg)
        print(stylize(text, colored.fg("cyan")), flush=True)

    def error(self, msg, tag="ERROR"):
        text = self.generate_text(self.identifier, tag, msg)
        print(stylize(text, colored.fg("red")), flush=True)

    def success(self, msg, tag="SUCCESS"):
        text = self.generate_text(self.identifier, tag, msg)
        print(stylize(text, colored.fg("green")), flush=True)
