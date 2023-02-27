fisier = open("data.txt", "r")

continut = fisier.read()

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

print(continut)
