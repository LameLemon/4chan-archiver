class Post:
    def __init__(self, name, date, message, pid, img_src=None, img_text=None, subject=None):
        self.name = name
        self.date = date
        self.message = message
        self.pid = pid
        self.img_src = img_src
        self.img_text = img_text
        self.subject = subject