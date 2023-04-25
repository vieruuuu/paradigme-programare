from HTMLFile import *
from JSONFile import *
from ArticleTextFile import *
from BlogTextFile import *
from TextFile import *

from FileFactory import *

if __name__ == "__main__":
    h: HTMLFile = FileFactory.factory("html")
    j: JSONFile = FileFactory.factory("json")
    b: BlogTextFile = FileFactory.factory("blog")
    a: ArticleTextFile = FileFactory.factory("article")

    h.read_file_from_stdin()
    j.read_file_from_stdin()
    b.read_file_from_stdin()
    a.read_file_from_stdin()

    h.print_html()
    j.print_json()
    b.print_text()
    a.print_text()
