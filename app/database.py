import json
from app.scientist import Scientist
from app.title import Title

class Database:
    def __init__(self, file):
        self.titles = []
        self.file = file

    def open(self):
        self.titles = []
        with open(self.file) as json_file:
            db = json.load(json_file)
            for entry in db:
                scientists = []
                for scientist in entry["scientists"]:
                    scientists.append(Scientist(scientist["name"]))
                self.titles.append(Title(entry["title"], scientists))

    def get_titles(self):
        return self.titles

    def to_str(self):
        str_titles = []
        for title in self.titles:
            str_titles.append(title.to_str())
        str_titles = str_titles.__str__().replace("\'", '')
        return "(Db " + str_titles + ")"