import os
import xml.etree.ElementTree as ET


class GenericFile:
    def get_path(self):
        raise NotImplementedError("`get_path` must be implemented")

    def get_freq(self):
        raise NotImplementedError("`get_path` must be implemented")


class TextASCII(GenericFile):
    def __init__(self, path_absolute, frequencies):
        self.path_absolute = path_absolute
        self.frequencies = frequencies

    def get_path(self):
        return self.path_absolute

    def get_freq(self):
        return self.frequencies


class XMLFile(TextASCII):
    def __init__(self, path_absolute, frequencies):
        TextASCII.__init__(self, path_absolute, frequencies)

        try:
            tree = ET.parse(self.path_absolute)
            self.first_tag = str(tree.getroot())
        finally:
            self.first_tag = None

    def get_first_tag(self):
        return self.first_tag


class TextUNICODE(GenericFile):
    def __init__(self, path_absolute, frequencies):
        self.path_absolute = path_absolute
        self.frequencies = frequencies

    def get_path(self):
        return self.path_absolute

    def get_freq(self):
        return self.frequencies


class Binary(GenericFile):
    def __init__(self, path_absolute, frequencies):
        self.path_absolute = path_absolute
        self.frequencies = frequencies

    def get_path(self):
        return self.path_absolute

    def get_freq(self):
        return self.frequencies


def is_ascii(content):
    freq = [1 for byte in content if byte in range(9, 10) or byte in range(13, 127)]
    ascii_freq = sum(freq) / len(content)

    return [ascii_freq > 0.9, freq]


def is_unicode(content):
    zero_freq = content.count(b"\x00") / len(content)

    return [zero_freq > 0.3, content.count(b"\x00")]


def is_binary(content):
    byte_freqs = [content.count(bytes([byte])) / len(content) for byte in range(256)]

    uniform_freq = all(abs(freq - 1 / 256) < 0.1 for freq in byte_freqs)

    return [uniform_freq, byte_freqs]


def check_file_type(file_path, content):
    if is_binary(content)[0]:
        return Binary(file_path, is_binary(content)[1])
    elif is_ascii(content)[0]:
        return TextASCII(file_path, is_ascii(content)[1])
    elif is_unicode(content)[0]:
        return TextUNICODE(file_path, is_unicode(content)[1])
    else:
        return None


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
for root, subdirs, files in os.walk(ROOT_DIR):
    for file in os.listdir(root):
        file_path = os.path.join(root, file)

        if os.path.isfile(file_path):
            # deschide fișierul spre acces binar
            f = open(file_path, "rb")

            try:
                content = f.read()

                result = check_file_type(file_path, content)

                if result == None:
                    print("Unknown file")
                else:
                    print(result)

            finally:
                f.close()
