from File import *
from HTMLFile import *
from JSONFile import *
from ArticleTextFile import *
from BlogTextFile import *
from TextFile import *


class FileFactory:
    @staticmethod
    def factory(file_type: str) -> File:
        match file_type:
            case "json":
                return JSONFile()
            case "html":
                return HTMLFile()
            case "article":
                return ArticleTextFile()
            case "blog":
                return BlogTextFile()
