from File import *


class JSONFile(File):
    def read_file_from_stdin(self):
        super().read_file_from_stdin()

    def print_json(self):
        result = "{\n"

        result += f'\t"title": "{self.title}"\n'
        result += f'\t"author": "{self.author}"\n'
        result += (
            '\t"paragraphs": ['
            + ", ".join(map(lambda p: '"' + p + '"', self.paragraphs))
            + "]"
        )

        result += "\n}"

        print(result)
