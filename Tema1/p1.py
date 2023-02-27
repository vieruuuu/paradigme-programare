from tkinter import *

expression = ""


def tokenize(text):
    lista = []

    i = 0
    while i < len(text):
        ch = text[i]

        if ch == "(":
            lista.append({"type": "("})
            i += 1
        elif ch == ")":
            lista.append({"type": ")"})
            i += 1
        elif ch == "+":
            lista.append(
                {
                    "type": "+",
                    "order": 1,
                }
            )
            i += 1
        elif ch == "-":
            lista.append(
                {
                    "type": "-",
                    "order": 1,
                }
            )
            i += 1
        elif ch == "*":
            lista.append(
                {
                    "type": "*",
                    "order": 2,
                }
            )
            i += 1
        elif ch == "/":
            lista.append(
                {
                    "type": "/",
                    "order": 2,
                }
            )
            i += 1
        else:
            number_start = i

            while i < len(text) and text[i].isdigit():
                i += 1

            lista.append(
                {"type": "number", "order": 0, "val": float(text[number_start:i])}
            )

    return lista


def calculate(tokens):
    result_str = ""

    for token in tokens:
        if token["type"] == "number":
            result_str += str(token["val"])
        else:
            result_str += token["type"]

    return float(str(eval(result_str)))


def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():

    global expression
    total = calculate(tokenize(expression))

    try:

        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = ""

        # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""

    # Function to clear the contents


# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    gui.configure(background="gray")

    gui.title("Simple Calculator")

    gui.geometry("420x140")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=5, ipadx=135)

    equation.set("")

    Button(
        gui,
        text=" 1 ",
        fg="white",
        bg="blue",
        command=lambda: press(1),
        height=1,
        width=7,
    ).grid(row=2, column=0)

    Button(
        gui,
        text=" 2 ",
        fg="white",
        bg="blue",
        command=lambda: press(2),
        height=1,
        width=7,
    ).grid(row=2, column=1)

    Button(
        gui,
        text=" 3 ",
        fg="white",
        bg="blue",
        command=lambda: press(3),
        height=1,
        width=7,
    ).grid(row=2, column=2)

    Button(
        gui,
        text=" 4 ",
        fg="white",
        bg="blue",
        command=lambda: press(4),
        height=1,
        width=7,
    ).grid(row=3, column=0)

    Button(
        gui,
        text=" 5 ",
        fg="white",
        bg="blue",
        command=lambda: press(5),
        height=1,
        width=7,
    ).grid(row=3, column=1)

    Button(
        gui,
        text=" 6 ",
        fg="white",
        bg="blue",
        command=lambda: press(6),
        height=1,
        width=7,
    ).grid(row=3, column=2)

    Button(
        gui,
        text=" 7 ",
        fg="white",
        bg="blue",
        command=lambda: press(7),
        height=1,
        width=7,
    ).grid(row=4, column=0)

    Button(
        gui,
        text=" 8 ",
        fg="white",
        bg="blue",
        command=lambda: press(8),
        height=1,
        width=7,
    ).grid(row=4, column=1)

    Button(
        gui,
        text=" 9 ",
        fg="white",
        bg="blue",
        command=lambda: press(9),
        height=1,
        width=7,
    ).grid(row=4, column=2)

    Button(
        gui,
        text=" 0 ",
        fg="white",
        bg="blue",
        command=lambda: press(0),
        height=1,
        width=7,
    ).grid(row=5, column=0)

    Button(
        gui,
        text=" + ",
        fg="white",
        bg="blue",
        command=lambda: press("+"),
        height=1,
        width=7,
    ).grid(row=2, column=3)

    Button(
        gui,
        text=" - ",
        fg="white",
        bg="blue",
        command=lambda: press("-"),
        height=1,
        width=7,
    ).grid(row=3, column=3)

    Button(
        gui,
        text=" * ",
        fg="white",
        bg="blue",
        command=lambda: press("*"),
        height=1,
        width=7,
    ).grid(row=4, column=3)

    Button(
        gui,
        text=" / ",
        fg="white",
        bg="blue",
        command=lambda: press("/"),
        height=1,
        width=7,
    ).grid(row=5, column=3)

    Button(
        gui,
        text=" ( ",
        fg="white",
        bg="blue",
        command=lambda: press("("),
        height=1,
        width=7,
    ).grid(row=2, column=4)

    Button(
        gui,
        text=" ) ",
        fg="white",
        bg="blue",
        command=lambda: press(")"),
        height=1,
        width=7,
    ).grid(row=3, column=4)

    Button(
        gui, text=" = ", fg="white", bg="blue", command=equalpress, height=1, width=7
    ).grid(row=5, column=1)

    Button(
        gui, text="Clear", fg="white", bg="blue", command=clear, height=1, width=7
    ).grid(row=5, column=2)

    # start the GUI
    gui.mainloop()
