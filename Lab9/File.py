from abc import ABC, abstractmethod


class File(ABC):
    title: str
    author: str
    paragraphs: list[str]

    def __init__(self) -> None:
        self.read_file_from_stdin()

    @abstractmethod
    def read_file_from_stdin(self):
        self.title = input("File title: ")
        self.author = input("File author: ")

        paragraphs_count = int(input("No of paragraphs: "))

        self.paragraphs = []

        for x in range(paragraphs_count):
            paragraph_content = input("Paragraph " + str(x) + ": ")

            self.paragraphs.append(paragraph_content)
