from TextFile import *


class BlogTextFile(TextFile):
    template: str = "BlogTextFile"

    def print_text(self):
        result = self.title + "\n"
        result += "\n".join(self.paragraphs) + "\n"
        result += "Written by: " + self.author + "\n"

        print(result)
