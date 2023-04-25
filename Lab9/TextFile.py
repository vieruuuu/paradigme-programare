from __future__ import annotations
from File import *
from copy import copy
from abc import abstractmethod


class TextFile(File):
    template: str = "TextFile"

    def read_file_from_stdin(self):
        super().read_file_from_stdin()

    @abstractmethod
    def print_text(self):
        result = "Template: " + self.template + "\n"
        result += "Title: " + self.title + "\n"
        result += "Autor: " + self.author + "\n"
        result += "Continut: \n" + "\n".join(self.paragraphs)

        print(result)

    def clone(self) -> TextFile:
        return copy(self)
