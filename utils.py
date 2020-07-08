from colored import stylize
from datetime import datetime
import colored

class Logger:
    def __init__(self, title, id_num=None):
        if id_num == None:
            self.identifier = "[{}]".format(title)
        else:
            self.identifier = "[{} {}]".format(title, id_num)

    def alert(self, msg, tag="ALERT"):
        current_time = datetime.now().strftime("%I:%M:%S.%f %p")
        text = "[{}] {} [{}] -> {}".format(current_time, self.identifier, tag, msg)
        print(stylize(text, colored.fg("magenta")))

    def info(self, msg, tag="INFO"):
        current_time = datetime.now().strftime("%I:%M:%S.%f %p")
        text = "[{}] {} [{}] -> {}".format(current_time, self.identifier, tag, msg)
        print(stylize(text, colored.fg("cyan")))

    def error(self, msg, tag="ERROR"):
        current_time = datetime.now().strftime("%I:%M:%S.%f %p")
        text = "[{}] {} [{}] -> {}".format(current_time, self.identifier, tag, msg)
        print(stylize(text, colored.fg("red")))

    def success(self, msg ,tag="SUCCESS"):
        current_time = datetime.now().strftime("%I:%M:%S.%f %p")
        text = "[{}] {} [{}] -> {}".format(current_time, self.identifier, tag, msg)
        print(stylize(text, colored.fg("green")))