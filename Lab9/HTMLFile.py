from File import *


class HTMLFile(File):
    def read_file_from_stdin(self):
        super().read_file_from_stdin()

    def print_html(self):
        result = f"""
<html>
<head>
  <title>{self.title}</title>
</head>

<body>
  <h1>{self.author}</h1>

{chr(10).join(map(lambda p: f"  <p>{p}</p>", self.paragraphs))  }
</body>
</html>"""

        print(result)
