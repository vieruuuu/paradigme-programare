#!/usr/bin/python3
import pathlib
import pygubu
import tkinter as tk
import re
import math

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Ex1.ui"


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


class Ex1App:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("Parser", master)

        self.integer_list_text = self.builder.get_object("integer_list_text")
        self.result_text = self.builder.get_object("result_text")

        self.builder.get_object("add_list_btn")["command"] = self.add_list
        self.builder.get_object("filter_odd_btn")["command"] = self.filter_odd
        self.builder.get_object("filter_primes_btn")["command"] = self.filter_primes
        self.builder.get_object("sum_numbers_btn")["command"] = self.sum_numbers

        builder.connect_callbacks(self)
        self.integer_list = []

    def display_result(self, text):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)

    def add_list(self):
        result = self.integer_list_text.get("1.0", tk.END)
        result = re.sub("\s+", "", result)
        result = [int(item) for item in result.split(",")]
        self.integer_list = result

        self.display_result(result)

    def filter_odd(self):
        self.integer_list = list(filter(lambda x: x % 2 != 0, self.integer_list))

        self.display_result(str(self.integer_list)[1:-1].replace(",", ""))

    def filter_primes(self):
        self.integer_list = list(filter(is_prime, self.integer_list))

        self.display_result(str(self.integer_list)[1:-1].replace(",", ""))

    def sum_numbers(self):
        self.display_result(sum(self.integer_list))

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Ex1App(root)
    app.run()
