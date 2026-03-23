class Logger:
    def __init__(self, file):
        self.f = open(file, "w")

    def log(self, msg):
        self.f.write(msg + "\n")

    def __del__(self):
        self.f.close()