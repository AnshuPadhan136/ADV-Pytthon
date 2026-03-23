class User:
    def __init__(self, name):
        self.name = name

class Post:
    count = 0
    def __init__(self, text):
        self.text = text
        Post.count += 1

class Comment:
    def __init__(self, text):
        self.text = text