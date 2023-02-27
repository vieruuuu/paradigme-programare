from pathlib import Path
import re

dirname = str(Path(__file__).parent.absolute())

fisier = open(dirname + "/data.txt", "r")

continut = fisier.read()

fisier.close()

vreau_sa_dispar = [
    ",",
    "<",
    ".",
    ">",
    "?",
    ";",
    ":",
    "'",
    '"',
    "-",
    "_",
    "(",
    ")",
    "/",
    "\\",
    "|",
]

for ch in vreau_sa_dispar:
    continut = continut.replace(ch, "")

continut = re.sub(" +", " ", continut)

print(continut)
