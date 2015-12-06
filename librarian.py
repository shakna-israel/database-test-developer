import uuid

class Book(object):
    def __init__(self):
        self.id = uuid.uuid4()
        self.title = "Untitled"
        self.author = ["Unknown"]
        self.length = 0

class Collection(object):
    def __init__(self):
        self.id = uuid.uuid4()
        self.title = "Untitled"
        self.author = ["Unknown"]
        self.length = 0
        self.count = 0
