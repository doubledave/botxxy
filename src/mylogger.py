import sys, time

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("botlog.log", "w", 0)

    def write(self, message):
        self.terminal.write(message)
        t = time.strftime('%H:%M:%S', time.localtime())
        self.log.write("[%s] %s" % (t, message))
        