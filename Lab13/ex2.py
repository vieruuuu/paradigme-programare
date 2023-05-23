class str(str):
    def toPascalCase(self):
        words = list(self.split(" "))

        return "".join(map(lambda w: w.capitalize(), words))


print(str("test sa vedem daca merge").toPascalCase())
