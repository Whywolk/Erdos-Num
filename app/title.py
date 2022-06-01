class Title:
    def __in1it__(self):
        self.title = ""
        self.scientists = []

    def __init__(self, title, scientists):
        self.title = title
        self.scientists = scientists

    def to_str(self):
        scientists = []
        for scientist in self.scientists:
            scientists.append(scientist.to_str())
        scientists = scientists.__str__().replace("\'", '')
        return '(' + scientists + ',"' + self.title + '")'