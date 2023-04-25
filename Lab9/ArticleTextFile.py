from TextFile import *


class ArticleTextFile(TextFile):
    template: str = "ArticleTextFile"

    def print_text(self):
        result = "                " + self.title + "\n"
        result += "                     by " + self.author + "\n"
        result += "\n".join(self.paragraphs)

        print(result)
