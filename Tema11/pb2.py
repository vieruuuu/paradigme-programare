from subprocess import run, PIPE

if __name__ == "__main__":
    command = input("run: ")

    commands: list[list[str]] = []

    # split commands
    for c in command.split("|"):
        c_new: list[str] = []

        # split by arguments
        for arg in c.split(" "):
            # remove whitespace
            if arg != "":
                c_new.append(arg)

        # add command
        commands.append(c_new)

    prev = run(commands[0], stdout=PIPE)

    for cmd in commands[1:]:
        prev = run(cmd, input=prev.stdout, stdout=PIPE)

    print(f'{prev.stdout.decode("utf-8")}')
